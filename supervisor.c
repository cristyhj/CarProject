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
    pid_t pidUI, otherPid;
    int fd;
    char *fifoFile = "/tmp/fifofile";
    char *pathToStart = "/home/sysop/CarProject/UserInterface/main.py";
    char *pathToMain = "/home/sysop/CarProject/main.sh";
    char *pathToNavit = "/home/sysop/CarProject/navit.sh";
    char buff[LEN];
    int over = 0;

    mkfifo(fifoFile, 0666);

    while (!over) {
        // prima data porneste programul UI
        pidUI = startProcess(pathToStart);

        // here continues the parent process
        //  si deschide fisierul pipe
        fd = open(fifoFile, O_RDONLY);

        // asteapta comanda de la parinte, sau alte procese
        while (1) {
            read(fd, buff, LEN);
            buff[10] = '\0';
            if (strcmp(buff, "start main") == 0) {
                // asteapta procesul curent sa se incheie
                //   procesul curent trebuie sa se incheie singur, fara semnal de kill
                //             poate in viitor voi implementa un timeout dupa care ii dau  force kill
                waitpid(pidUI, 0, 0);
                // dupa care porneste procesul destinat
                otherPid = startProcess(pathToMain);
                waitpid(otherPid, 0, 0);
                break;
            }
            if (strcmp(buff, "start navi") == 0) {
                waitpid(pidUI, 0, 0);
                otherPid = startProcess(pathToNavit);
                waitpid(otherPid, 0, 0);
                break;
            }
            if (strcmp(buff, "start shut") == 0) {
                over = 1;
                break;
            }
        }
    }
    // clean
    unlink(fifoFile);
    return 0;
}
