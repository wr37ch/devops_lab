import argparse
import getpass
import requests
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='%(prog)s 1.3')
parser.add_argument('-u','--user', type=str, help='user in which you are interested. ex: -u wr37ch')
parser.add_argument('-c','--comments', type=str, help='display number of comments. ex: -c comments')
parser.add_argument('-s','--status', type=str, help='display numbers of users pull requests, ex: -s status')
parser.add_argument('-a','--additions', type=str, help='display number of additions, ex: -a additions')
parser.add_argument('-d','--deletions', type=str, help='display number of deletions, ex: -d deletions')
parser.add_argument('-o','--opener', type=str, help='shows who opened PR. ex: -o opener')
parser.add_argument('-q','--quitter', type=str, help='shows who closed PR. ex: -q closer)')
parser.add_argument('-t','--datetime', type=str, help='display time between opening and closing ex: (-t datetime)')
parser.add_argument('-user','--githubuser', type=str, help='git username, ex: -user alenapy')
parser.add_argument('-rep','--githubrepo', type=str, help='git repo, ex: -rep devops_lab)')

args = parser.parse_args()

print("Sample how to execute script 'python githubstats.py -u wr37ch -c comments -a additions -d deletions -t datetime -user alenapy -rep devops_lab -o opener -q quitter'")

user = str(args.user)
c = str(args.comments)
s = str(args.status)
a = str(args.additions)
d = str(args.deletions)
t = str(args.datetime)
o = str(args.opener)
q = str(args.quitter)
gh_user = str(args.githubuser)
gh_repo = str(args.githubrepo)

username = input("What's your username? ")
password = getpass.getpass(prompt='Enter your password ')


if s == 'status':
    print("Statistic on Pull Request from repository")
    for x in range(3):
        r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100', auth=(username, password))
        re = r.json()
        open_PR = 0
        close_PR = 0
        for x in re:
            if x['state'] == 'open':
                open_PR += 1
            else:
                close_PR += 1
    print(str(open_PR) + "PR are open " + str(close_PR) +"PR are closed")
    print('\n')


if user == user:
    print("Pull Requests from the user" )
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100',
                     auth=('wr37ch', password))
    re = r.json()
    for x in re:
        if x['user']['login'] == user:
            print('PR №' + str(x['number']), 'was created at ' + str(datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%YT%H:%M:%SZ")), "and it's state is " + str(x['state']))
    print('\n')


if o == 'quitter':
    print("Who created Pull Requests" )
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100',
                     auth=('wr37ch', password))
    re = r.json()
    for z in re:
        if z['user']['login'] == user:
            numba = z['number']
            r1 = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls/' + str(numba),
                              auth=('wr37ch', password))
            re1 = r1.json()
            print("User", re1['user']['login'], "opened PR number " + str(numba))
    print('\n')

if q == 'closer':
    print("Who closed Pull Requests" )
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100',
                     auth=('wr37ch', password))
    re = r.json()
    for z in re:
        if z['user']['login'] == user:
            numba = z['number']
            r1 = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls/' + str(numba),
                              auth=('wr37ch', password))
            re1 = r1.json()
            if re1['merged_by'] is not None:
                print("User", re1['merged_by']['login'], "merged PR number " + str(numba))
            else:
                print("PR number " + str(numba) + " is still not merged")
    print('\n')

if c == 'comments':
    print("Number of comments under the PR")
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100', auth=('wr37ch', password))
    re = r.json()
    for z in re:
        if z['user']['login'] == user:
            numba = z['number']
            r1 = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls/' + str(numba),
                             auth=('wr37ch', password))
            re1 = r1.json()
            print(re1['review_comments'], "comments under the PR number " +str(numba))
    print('\n')


if a == 'additions':
    print("Number of added lines" )
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100',auth=('wr37ch', password))
    re = r.json()
    for z in re:
        if z['user']['login'] == user:
            numba = z['number']
            r1 = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls/' + str(numba),
                             auth=('wr37ch', password))
            re1 = r1.json()
            print(re1['additions'], "additions in PR number " +str(numba))
    print('\n')

if d == 'deletions':
    print("Number of removed lines")
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100', auth=('wr37ch', password))
    re = r.json()
    for z in re:
        if z['user']['login'] == user:
            numba = z['number']
            r1 = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls/' + str(numba),
                             auth=('wr37ch', password))
            re1 = r1.json()
            print(re1['deletions'], "deletions in PR number " +str(numba))
    print('\n')

if t == 'datetime':
    print("Number of days between opening and closing of the PR" )
    r = requests.get('https://api.github.com/repos/'+str(gh_user)+'/'+str(gh_repo)+'/pulls?state=all&page=1&per_page=100',
                     auth=('wr37ch', password))
    re = r.json()
    for x in re:
        if x['user']['login'] == user:
            if x['state'] == 'closed':
                ct = datetime.datetime.now()
                date = datetime.datetime.strptime(x['closed_at'], "%Y-%m-%dT%H:%M:%SZ")
                res = ct - date
                print("PR " + str(x['number']) + ' was closed after ' + str(res.days) + " days")
    print('\n')

