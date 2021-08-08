from git import Repo

PATH_OF_GIT_REPO = r'C:\Users\carot\Desktop\Netlify-trial'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_Push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        Origin = repo.remote(name='Origin')
        Origin.Push()
    except:
        print('Some error occured while pushing the code')    


git_Push()