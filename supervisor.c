#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define LEN 64

    // start another process as a child
void startProcess(const char *path) {
    int childPid = fork();
    if (childPid == -1) {
        printf("fork error\n");
        return 1;
    } else if (childPid == 0) {
        // here starts the UI program as a child process
        execv(path, (char*const*)NULL);
        printf("continua aparent\n");
    }
    // here continues the parent process
    return;
}

int main() {
    int childPid;
    int fd;
    char *fifoFile = "/tmp/fifofile";
    char *pathToStart = "/media/andrei/Data/ProgramsData/Python/CarProject/UI/start.py";
    char *pathToMain = "/media/andrei/Data/ProgramsData/Python/CarProject/DashBoard/main.py";
    char *pathToNavit = "/home/sysop/navit-build/navit/navit";
    char buff[LEN];
    
    mkfifo(fifoFile, 0666);
    
    startProcess(pathToStart);
    
    // here continues the parent process
    fd = open(fifoFile, O_RDONLY);
    while (1) {
        read(fd, buff, LEN);
        buff[10] = '\0';
        if (strcmp(buff, "start main") == 0) {
            startProcess(pathToMain);
            break;
        }
        if (strcmp(buff, "start navi") == 0) {
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
