#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

#define LEN 64

    // start another process as a child
pid_t startProcess(const char *path) {
    pid_t childPid = fork();
    if (childPid == -1) {
        printf("fork error\n");
        return -1;
    } else if (childPid == 0) {
        // here starts the UI program as a child process
        execv(path, (char*const*)NULL);
        printf("continua aparent (adica e eroare - nu s-a deschis path-ul: %s!\n", path);
    }
    // here continues the parent process
    return childPid;
}

int main() {
    pid_t pidUI;
    int fd;
    char *fifoFile = "/tmp/fifofile";
    char *pathToStart = "/media/andrei/Data/ProgramsData/Python/CarProject/UI/start.py";
    char *pathToMain = "/media/andrei/Data/ProgramsData/Python/CarProject/DashBoard/main.py";
    char *pathToNavit = "/home/sysop/navit-build/navit/navit";
    char buff[LEN];
    
    mkfifo(fifoFile, 0666);
    
    // prima data porneste programul UI
    pidUI = startProcess(pathToStart);
    
    // here continues the parent process
    fd = open(fifoFile, O_RDONLY);
    
    // asteapta comanda de la parinte, sau alte procese
    while (1) {
        read(fd, buff, LEN);
        buff[10] = '\0';
        if (strcmp(buff, "start main") == 0) {
            waitpid(pidUI, 0, 0);
            startProcess(pathToMain);
            break;
        }
        if (strcmp(buff, "start navi") == 0) {
            waitpid(pidUI, 0, 0);
            startProcess(pathToNavit);
            break;
        }
        if (strcmp(buff, "start shut") == 0) {
            break;
        }
    }
    
    
    // clean
    unlink(fifoFile);
    return 0;
}
