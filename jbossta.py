from watchdog.events import FileSystemEventHandler
import sys, os, glob, shutil, time

class CopyEventHandler(FileSystemEventHandler):

    def __init__(self, working_path, dest_path):
        self.__working_path__ = working_path
        self.__dest_path__ = dest_path
    
    def on_modified(self, event):
        print self.__working_path__
        print self.__dest_path__
        print 'copiando ' + event.src_path
        origem = event.src_path
        destino = self.__dest_path__+'\\'+origem.replace(self.__working_path__, '')
        shutil.copy2(origem, destino)

def get_tmp_dir(appname):
    search_dir = os.getenv('JBOSS_HOME') + r"\server\default\tmp"
    dirs = filter(os.path.isdir, glob.glob(search_dir +'\\*'))
    
    directory_tuple_list = [(d,os.path.getmtime(d)) for d in dirs]
    directory_tuple_list.sort(key=lambda x: x[1], reverse=True)
    
    for d in directory_tuple_list:
        directory = d[0] + '\\' + appname
        if os.path.exists(directory):
            return directory


def main():
    from watchdog.observers import Observer
    
    path = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
    appname = sys.argv[1]
    
    tmp_dir = get_tmp_dir(appname)
    if tmp_dir is None:
        print 'Tmp nao encontrado'
        sys.exit(0)
    
    observer = Observer()
    observer.schedule(CopyEventHandler(path, tmp_dir), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    