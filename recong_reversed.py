import collections
import re
import urllib2


# return html data for given url
def get_page_by_url(url):
    headers = {}
    headers[
        'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    page = response.read()
    return page


def get_img_caps_list(given_img_url):
    url = 'https://www.google.com/searchbyimage?&image_url=' + given_img_url
    # time.sleep = 0.1
    print 'reverse search: ' + url

    # parse source
    source = get_page_by_url(url)

    # get url for "more visually similar images"
    similar_img_url = source.split('">Visually similar images')[0].split('<a href="')[-1]
    more_img_url = 'https://www.google.com' + similar_img_url
    more_img_url = ''.join(more_img_url.split('amp;'))
    print 'Visually similar images: ' + more_img_url

    # list of all images caps
    list_caps = []

    # parse similar image page
    try:
        res_page = get_page_by_url(more_img_url)
        if 'class="rg_di' in res_page:

            # in case want to limit num of images
            num_image = 0
            # get list of div classes have title info, exclude first one
            img_data_list = res_page.split('<div class="rg_meta">')[1:]
            # print('len:' + str(len(img_data_list)))

            while num_image < len(img_data_list) - 1:
                # while num_image < 20:
                cur_data = img_data_list[num_image + 1]
                # parse list and get title info
                img_cap = cur_data.split('","s":"')[1].split('","th":')[0]
                num_image += 1

                # to get rid of some edge cases
                if len(img_cap) < 200:
                    # clean captions
                    img_cap = re.sub('\W', ' ', img_cap)
                    # u0026 39 is eqivalent to '
                    img_cap = ''.join(img_cap.split('u0026 39'))
                    # clear multiple whitespace
                    img_cap = ' '.join(img_cap.split())
                    # print('link: ' + img_cap)

                    # add cleaned caps to list
                    for word in img_cap.split():
                        list_caps.append(word.lower())

        else:
            print("No link found")
    except Exception as e:
        print 'exception:' + str(e)

    return list_caps


# given_img_url = 'http://i.imgur.com/LdkDKmy.png'
# given_img_url = 'http://vignette1.wikia.nocookie.net/evangelion/images/1/12/Rei_Ayanami_OP.png/revision/latest?cb=20120608122803'
given_img_url = 'http://www.blogcdn.com/www.engadget.com/media/2012/09/boston-dynamics-alphadog-ls3-darpa-demo.jpg'
img_caps_list = get_img_caps_list(given_img_url)

# clean data
import clean_data

img_caps_list = clean_data.clean_data_(img_caps_list)
counter = collections.Counter(img_caps_list)
print(counter.most_common())
