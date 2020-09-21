#!/bin/sh
# Convert a raw binary image into an ELF file suitable for loading into a disassembler

section_name=$3
cat > raw$$.ld <<EOF
SECTIONS
{
EOF

# echo " . = $section_name;" >> raw$$.ld

cat >> raw$$.ld <<EOF
  .text : { *(.text) }
}
EOF

# CROSS_PREFIX=arm-none-eabi-
CROSS_PREFIX=arm-linux-gnueabihf-
ld_output_file_name=$1
bin_output_file_name=$2


${CROSS_PREFIX}ld -b binary -r -o raw$$.elf $ld_output_file_name
${CROSS_PREFIX}objcopy  --rename-section .data=.text \
                        --set-section-flags .data=alloc,code,load raw$$.elf
${CROSS_PREFIX}ld raw$$.elf -o $bin_output_file_name
# ${CROSS_PREFIX}ld raw$$.elf -T raw$$.ld -o $bin_output_file_name
# ${CROSS_PREFIX}strip -s $bin_output_file_name

rm -rf raw$$.elf 
