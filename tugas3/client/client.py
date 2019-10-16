import Pyro4
import subprocess

def get_server():
    #ganti "localhost dengan ip yang akan anda gunakan sebagai server" 
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    return gserver

def list_command():
    print('List Command : ')
    print('list = Melihat list file yang ada di dalam server')
    print('create <namafile> = Membuat file baru')
    print('delete <namafile> = Menghapus file')
    print('read <namafile> = Membaca isi file yang ada')
    print('exit = Keluar')


if __name__=='__main__':
    server = get_server()
    if server == None:
        exit()
    connected = True
    while connected:
        req = input ("> ").lower()
        req_split = req.split()
        if req_split[0] == 'list':
            print(server.get_list_dir(req))
        elif req_split[0] == 'create':
            print(server.create_handler(req))
        elif req_split[0] == 'delete':
            print(server.delete_handler(req))
        elif req_split[0] == 'read':
            print(server.read_handler(req))
        elif req_split[0] == 'update':
            print(server.update_handler(req))
        elif req_split[0] == 'exit':
            print(server.bye())
            connected = False
        elif req_split[0] == '--help':
            list_command()
        else:
            print(server.command_not_found())
