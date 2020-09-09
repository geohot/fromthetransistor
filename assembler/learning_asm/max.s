.section .text
.global _start

_start:
    push {r11, lr}    /* Start of the prologue. Saving Frame Pointer and LR onto the stack. r11=frame pointer, lr=link register*/ 
    add r11, sp, #0   /* Setting up the bottom of the stack frame sp=stack pointer/
    sub sp, sp, #16   /* End of the prologue. Allocating some buffer on the stack */
    mov r0, #1        /* setting up local variables (a=1). This also serves as setting up the first parameter for the max function */
    mov r1, #2        /* setting up local variables (b=2). This also serves as setting up the second parameter for the max function */
    bl max            /* Calling/branching to function max */
    sub sp, r11, #0   /* Start of the epilogue. Readjusting the Stack Pointer */
    pop {r11, pc}     /* End of the epilogue. Restoring Frame pointer from the stack, jumping to previously saved LR via direct load into PC */

max:
    push {r11}        /* Start of the prologue. Saving Frame Pointer onto the stack */
    add r11, sp, #0   /* Setting up the bottom of the stack frame */
    sub sp, sp, #12   /* End of the prologue. Allocating some buffer on the stack */
    cmp r0, r1        /* Implementation of if(a<b) */
    movlt r0, r1      /* if r0 was lower than r1, store r1 into r0 */
    add sp, r11, #0   /* Start of the epilogue. Readjusting the Stack Pointer */
    pop {r11}         /* restoring frame pointer */
    bx lr             /* End of the epilogue. Jumping back to main via LR register */
