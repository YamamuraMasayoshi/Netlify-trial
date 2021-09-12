import os
import git

#Pushしたいリポジトリに移動
os.chdir(r'C:\Users\carot\OneDrive\デスクトップ\Netlify-trial')
repo = git.Repo()

#最新を取り込むため一旦PullC:\Users\carot\OneDrive\デスクトップ\Netlify-trial
o = repo.remotes.origin
o.pull()

#Commit(サブディレクトリ含めて全て)
repo.git.commit('.','-m','\"Commit Log\"')

#Push
origin = repo.remote(name='origin')
origin.push()