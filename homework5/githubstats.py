import argparse
import getpass
import requests
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='%(prog)s 1.3')
parser.add_argument('-u','--user', type=str, help='user in which you are interested. ex: -u wr37ch')
parser.add_argument('-c','--comments',action='store_true', help='display number of comments. ex: -c or --comments ')
parser.add_argument('-s','--status', action='store_true', help='display numbers of users pull requests, ex: -s or --status ')
parser.add_argument('-a','--additions', action='store_true', help='display number of additions, ex: -a or --additions')
parser.add_argument('-d','--deletions', action='store_true', help='display number of deletions, ex: -d or --deletions')
parser.add_argument('-o','--opener', action='store_true', help='shows who opened PR. ex: -o or --opener')
parser.add_argument('-q','--quitter', action='store_true', help='shows who closed PR. ex: -q or --quitter)')
parser.add_argument('-t','--datetime', action='store_true', help='display time between opening and closing ex: -t or --datetime')
parser.add_argument('-user','--githubuser', type=str, help='git username, ex: -user alenapy')
parser.add_argument('-rep','--githubrepo', type=str, help='git repo, ex: -rep devops_lab)')

args = parser.parse_args()

print("Sample how to execute script 'python githubstats.py -u wr37ch -c -a -d -t -user alenapy -rep devops_lab -o -q -s'")

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
repo_link = 'https://api.github.com/repos/{}/{}/pulls?state=all&page=1&per_page=100'.format(gh_user, gh_repo)
pr_link = 'https://api.github.com/repos/{}/{}/pulls/{}'


if args.status:
    print("Statistic on Pull Request from repository")
    for x in range(3):
        r = requests.get(repo_link, auth=(username, password))
        re = r.json()
    open_PR = 0
    close_PR = 0
    for x in re:
        if x['state'] == 'open':
            open_PR += 1
        else:
            close_PR += 1
    print("{} PR are open. {} PR are closed".format(open_PR,close_PR))
    print('\n')


if args.user:
    print("Pull Requests from the user" )
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for x in re:
        if x['user']['login'] == user:
            print("PR # {} was created at {} and its state is {}".format(x['number'],datetime.datetime.strptime(x['created_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%YT%H:%M:%SZ"),x['state']))
    print('\n')


if args.opener:
    print("Who created Pull Requests" )
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for i in re:
        if i['user']['login'] == user:
            numba = i['number']
            r1 = requests.get(pr_link.format(gh_user,gh_repo,numba),
                              auth=(username, password))
            re1 = r1.json()
            print("User {} opened PR number {}".format(re1['user']['login'], numba))
    print('\n')

if args.quitter:
    print("Who closed Pull Requests" )
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for i in re:
        if i['user']['login'] == user:
            numba = i['number']
            r1 = requests.get(pr_link.format(gh_user,gh_repo,numba),
                              auth=(username, password))
            re1 = r1.json()
            if re1['merged_by'] is not None:
                print("User {} merged PR number {}".format(re1['merged_by']['login'],numba))
            else:
                print("PR number {} is still not merged".format(numba))
    print('\n')

if args.comments:
    print("Number of comments under the PR")
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for i in re:
        if i['user']['login'] == user:
            numba = i['number']
            r1 = requests.get(pr_link.format(gh_user,gh_repo,numba),
                             auth=(username, password))
            re1 = r1.json()
            print("{} comments under the PR number {}".format(re1['review_comments'],numba))
    print('\n')


if args.additions:
    print("Number of added lines" )
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for i in re:
        if i['user']['login'] == user:
            numba = i['number']
            r1 = requests.get(pr_link.format(gh_user,gh_repo,numba),
                             auth=(username, password))
            re1 = r1.json()
            print("{} additions in PR number {}".format(re1['additions'], numba))
    print('\n')

if args.deletions:
    print("Number of removed lines")
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for i in re:
        if i['user']['login'] == user:
            numba = i['number']
            r1 = requests.get(pr_link.format(gh_user,gh_repo,numba),
                             auth=(username, password))
            re1 = r1.json()
            print("{} deletions in PR number {}".format(re1['deletions'],numba))
    print('\n')

if args.datetime:
    print("Number of days between opening and closing of the PR" )
    r = requests.get(repo_link, auth=(username, password))
    re = r.json()
    for x in re:
        if x['user']['login'] == user:
            if x['state'] == 'closed':
                current_time = datetime.datetime.now()
                date = datetime.datetime.strptime(x['closed_at'], "%Y-%m-%dT%H:%M:%SZ")
                res = current_time - date
                print("PR {} was closed after {} days".format(x['number'],res.days))
    print('\n')

