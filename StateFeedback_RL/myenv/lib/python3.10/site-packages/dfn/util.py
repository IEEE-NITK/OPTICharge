import requests
from tqdm import tqdm

PUBLIC_PREFIX = "https://disk.sophgo.vip"
def fix_url(url):
    prefix = url.split('/')[2]
    return PUBLIC_PREFIX+url.split(prefix)[1]

def judge(url):
    return url.split("/")[3] == "sharing"

def _get_file_name(url):
    if judge(url):
        id = url.split('/')[4]
        file_name_url = PUBLIC_PREFIX+"/sharing/webapi/entry.cgi?api=SYNO.Core.Sharing.Session&version=1&method=get&sharing_id=%22{}%22".format(id)
        file_name = requests.get(file_name_url).text.split('filename" : "')[1].split('"')[0]
    else:
        file_name = url.split("/")[-1]
    return file_name

def get_id(url):
    return url.split("/")[4]

def _get_sharing_id(url):
    res = requests.get(url)
    sharing_id = res.headers['Set-Cookie'].split('=')[1].split(';')[0]
    return sharing_id

def get_sharing_id(url):
    file_name = _get_file_name(url)
    if judge(url):
        sharing_id = _get_sharing_id(url)
    else:
        converted_url = url_convert(url)
        sharing_id = _get_sharing_id(converted_url)
    return sharing_id

def judge_if_need_process(url):
    if judge(url):
        file_name = _get_file_name(url)
        if len(file_name.split(".")) == 1:
            return "dir_o"
        else :
            return "single"
    else:
        return "dir"

def url_convert(url):
    if judge(url):
        ulist = url.split("/")
        converted_url = PUBLIC_PREFIX + "/fsdownload/" + get_id(url) + "/" + _get_file_name(url)
        return converted_url
    else:
        ulist = url.split("/")
        converted_url = PUBLIC_PREFIX + "/sharing/" + get_id(url)
        return converted_url

def get_file_name(url):
    return _get_file_name(url)+".zip" if judge_if_need_process(url) != "single" else _get_file_name(url)

def get_curl_cmd(url):
    fixed_url = fix_url(url)
    sharing_id = get_sharing_id(fixed_url)
    file_name = get_file_name(fixed_url)
    id = get_id(fixed_url)
    if judge_if_need_process(fixed_url) == "single":
        curl_cmd = 'curl -o ' + file_name + ' -b "sharing_sid=' + sharing_id \
            + '" "' + url_convert(fixed_url) + '"'
    else:
        post_data = "api=SYNO.FolderSharing.Download&method=download&version=2&mode=download&stdhtml=false&dlname=%22" \
            + file_name + "%22&path=%5B%22%2F" + file_name.split(".")[0] + "%22%5D&_sharing_id=%22" + id + "%22&codepage=chs"
        curl_cmd = 'curl -o ' + file_name + ' -H "Content-Type: application/x-www-form-urlencoded" -b "sharing_sid=' + sharing_id \
            + '" -X POST -d "' + post_data + '" "' + PUBLIC_PREFIX + '/fsdownload/webapi/file_download.cgi/' + file_name + '"'
    return curl_cmd

def download_from_nas(url):
    def download(resp, url):
        total = int(resp.headers.get('content-length', 0))
        fname = get_file_name(url)
        with open(fname, 'wb') as file, tqdm(
                desc=fname,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
    fixed_url = fix_url(url)
    sharing_id = get_sharing_id(fixed_url)
    file_name = get_file_name(fixed_url)
    id = get_id(fixed_url)
    cookie = {
        "sharing_sid":sharing_id
    }
    if judge_if_need_process(url) == "single":
        resp = requests.get( url = url_convert(fixed_url),cookies = cookie, stream=True)
        download(resp, fixed_url)
    else:
        url = PUBLIC_PREFIX + '/fsdownload/webapi/file_download.cgi/' + file_name
        post_data = "api=SYNO.FolderSharing.Download&method=download&version=2&mode=download&stdhtml=false&dlname=%22" \
                + file_name + "%22&path=%5B%22%2F" + file_name.split(".")[0] + "%22%5D&_sharing_id=%22" + id + "%22&codepage=chs"
        resp = requests.post( url = url,cookies = cookie, data = post_data, stream=True)
        download(resp, fixed_url)
    

if __name__ == "__main__":
    single = "http://219.142.246.77:65000/sharing/lLojTQ9xW"
    multi = "https://disk.sophgo.vip/fsdownload/eqwC92lRU/vit"
    multi_o = "https://disk.sophgo.vip/sharing/qHL626Irz"
    print(fix_url(single))