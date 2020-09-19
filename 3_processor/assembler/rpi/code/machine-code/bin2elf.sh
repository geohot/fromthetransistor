#!/bin/sh
# Convert a raw binary image into an ELF file suitable for loading into a disassembler

cat > raw$$.ld <<EOF
SECTIONS
{
EOF

echo " . = $3;" >> raw$$.ld

cat >> raw$$.ld <<EOF
  .text : { *(.text) }
}
EOF

CROSS_PREFIX=arm-none-eabi-

${CROSS_PREFIX}ld -b binary -r -o raw$$.elf $1
${CROSS_PREFIX}objcopy  --rename-section .data=.text \
                        --set-section-flags .data=alloc,code,load raw$$.elf
${CROSS_PREFIX}ld raw$$.elf -T raw$$.ld -o $2
${CROSS_PREFIX}strip -s $2

rm -rf raw$$.elf 
