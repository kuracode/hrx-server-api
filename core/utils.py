import requests
from bs4 import BeautifulSoup

def all_games():
    URL = "https://status.hirezstudios.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    index = [0, 1, 2, 8, 14, 20]

    names_lst = []
    names = soup.find_all("span", class_="name")
    for name in names:
        names_lst.append(name.text.strip())
    names_lst = [i for j, i in enumerate(names_lst) if j not in index]

    status_lst = []
    statuses = soup.find_all("span", class_="component-status")
    for status in statuses:
        status_lst.append(status.text.strip())
    status_lst = [i for j, i in enumerate(status_lst) if j not in index]

    res = [{'Game': n, 'Status': s} for n, s in zip(names_lst, status_lst)]
    return res

def smite():
    URL = "https://status.hirezstudios.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    index = [3, 4, 5, 6, 7]

    names_lst = []
    names = soup.find_all("span", class_="name")
    for name in names:
        names_lst.append(name.text.strip())
    names_lst = [i for j, i in enumerate(names_lst) if j in index]

    status_lst = []
    statuses = soup.find_all("span", class_="component-status")
    for status in statuses:
        status_lst.append(status.text.strip())
    status_lst = [i for j, i in enumerate(status_lst) if j in index]

    res = [{'Game': n, 'Status': s} for n, s in zip(names_lst, status_lst)]
    return res

def rogue_company():
    URL = "https://status.hirezstudios.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    index = [9, 10, 11, 12, 13]

    names_lst = []
    names = soup.find_all("span", class_="name")
    for name in names:
        names_lst.append(name.text.strip())
    names_lst = [i for j, i in enumerate(names_lst) if j in index]

    status_lst = []
    statuses = soup.find_all("span", class_="component-status")
    for status in statuses:
        status_lst.append(status.text.strip())
    status_lst = [i for j, i in enumerate(status_lst) if j in index]

    res = [{'Game': n, 'Status': s} for n, s in zip(names_lst, status_lst)]
    return res

def paladins():
    URL = "https://status.hirezstudios.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    index = [15, 16, 17, 18, 19]

    names_lst = []
    names = soup.find_all("span", class_="name")
    for name in names:
        names_lst.append(name.text.strip())
    names_lst = [i for j, i in enumerate(names_lst) if j in index]

    status_lst = []
    statuses = soup.find_all("span", class_="component-status")
    for status in statuses:
        status_lst.append(status.text.strip())
    status_lst = [i for j, i in enumerate(status_lst) if j in index]

    res = [{'Game': n, 'Status': s} for n, s in zip(names_lst, status_lst)]
    return res

def realm_royale():
    URL = "https://status.hirezstudios.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    index = [21, 22, 23, 24, 25]

    names_lst = []
    names = soup.find_all("span", class_="name")
    for name in names:
        names_lst.append(name.text.strip())
    names_lst = [i for j, i in enumerate(names_lst) if j in index]

    status_lst = []
    statuses = soup.find_all("span", class_="component-status")
    for status in statuses:
        status_lst.append(status.text.strip())
    status_lst = [i for j, i in enumerate(status_lst) if j in index]

    res = [{'Game': n, 'Status': s} for n, s in zip(names_lst, status_lst)]
    return res