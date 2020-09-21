.data
var1: .word 3
var2: .word 4

.text
.global _start

_start:
    ldr %r0, adr_var1  /* @ load the memory address of var1 via label adr_var1 into R0 */
    ldr %r1, adr_var2  /* @ load the memory address of var2 via label adr_var2 into R1 */
    ldr %r2, [%r0]      /* @ load the value (0x03) at memory address found in R0 to register R2  r2 = *r0 = 1 */
    str %r2, [%r1, $2]  /* @ address mode: offset. Store the value found in R2 (0x03) to the memory address found in R1 plus 2. Base register (R1) unmodified. r2 = *r3 */
    str %r2, [%r1, $4]! /* @ address mode: pre-indexed. Store the value found in R2 (0x03) to the memory address found in R1 plus 4. Base register (R1) modified: R1 = R1+4 . (r1+4): r5=*r2 */
    ldr %r3, [%r1], $4  /*address mode: post-indexed. Load the value at memory address found in R1 to register R3. Base register (R1) modified: R1 = R1+4  r3 = *(r1+4) = *r5 */
    bkpt

adr_var1: .word var1
adr_var2: .word var2
