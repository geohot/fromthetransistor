program=$1

as ${program}.s -o ${program}.o && ld ${program}.o -o ${program} && ./${program}
