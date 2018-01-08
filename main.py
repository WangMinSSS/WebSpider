
if __name__ == '__main__':
    main_url = 'http://www.dytt8.net/'
    text = GetHtml(main_url)
    soup = OpeHtml(text)

    urls = []
    for i in soup.find_all('a'):
        if re.match(r'^/html/gndy/dyzz/', i['href']):
            urls.append(i['href'])

    urls = list(set(urls))
    urls.sort(reverse=True)
    urls = urls[1:]

    f = open('moive.txt', 'w')
    f.truncate()

    for u in urls:
        s = GetHtml(main_url + u)
        s = OpeHtml(s)

        for i in s.find(id='Zoom').strings:
            f.write(i)

        f.write('%%%%%%%%%%%%%%%%%%%%%%%%%')
    f.close()