from lxml import html

with open(r'C:\Users\Tim\Desktop\news.html', "r") as f:
    page = f.read()
tree = html.fromstring(page)

# file1 = open("newlist.dat", "a")  # append mode

for i in range(1,36):
    title = tree.xpath(f'/html/body/div/div/div/div[{i}]/h2')
    date = tree.xpath(f'/html/body/div/div/div/div[{i}]/p')
    subtitle = tree.xpath(f'/html/body/div/div/div/div[{i}]/h5/a/text()')
    link = tree.xpath(f'/html/body/div/div/div/div[{i}]/h5/a/@href')

    #print(title[0].text.strip())

    title_string = title[0].text.strip()

    if not date:
      # print("no date")
      date_string = ""
    else:
      # print(date[0].text)
      date_string = date[0].text

    if not subtitle:
      # print("no sub")
      sub_string = ""
    else:
      #print(subtitle[0])
      sub_string = subtitle[0].strip()

    if not link:
      #print("no link")
      link_string = ""
      print(f'**[{date_string}]** {title_string}: {sub_string}. \n')
    else:
      #print(link[0])
      link_string = link[0]

      print(f'**[{date_string}]** {title_string}: [{sub_string}]({link_string}). \n')

    #file1.write(f'**[{date}]** Paper Accepted at ACM IMWUT (Ubicomp) 2019: [To Mask or Not to Mask? Balancing Privacy with Visual Confirmation Utility in Activity-Oriented Wearable Cameras](https://dl.acm.org/citation.cfm?id=3351230). \n")
    # file1.close()

