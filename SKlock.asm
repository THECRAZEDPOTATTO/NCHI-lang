    org 0x7c00
    jmp main

Shutdown:
    mov ax, 0x1000
    mov ax, ss
    mov sp, 0xf000
    mov ax, 0x5307
    mov bx, 0x0001
    mov cx, 0x0003
    int 0x15

WaitForEnter:
    mov ah, 0
    int 0x16
    cmp al, 0x0D
    jne WaitForEnter
    ret

main:   
    call WaitForEnter
    call Shutdown

times 510-($-$$) db 0
dw 0xaa55
