# Adder - 80 points

This program adds numbers. Find the flag! [adder](https://github.com/EasyCTF/easyctf-iv-problems/raw/master/adder/adder)

hint: Adds numbers

### Solution
###### Writeup by asinggih

The program requires me to input 3 numbers, and at the end it prints out ```nope```

```sh
❯ ./adder
Enter three numbers!
12
15
6
nope.

```
From the given situation, it seems that the program requires us to input the correct sum of numbers, and then it will spit us the flag. However, at that stage I still didn't know what was the "correct" sum. With my current knowldge i only have 3 possible ways to know the correct sum:

- Brute force the numbers (It's gonna take too long! what if the sum is a really really large number??)
- Look at the source code (Not a viable option, since it's not provided)
- Reverse engineer the executable file (The one that i actually did)

I did a bit of googling in reverse engineering an executable file, and [one of the sources](https://null-byte.wonderhowto.com/how-to/reverse-engineering-with-radare2-a-quick-introduction-0165996/) suggested that I should utilise radare2 to perform the reverse engineering process.

```sh
❯ r2 adder 
[0x00400860]> aa
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x00400860]> pdf@sym.main
            ;-- main:
/ (fcn) main 208
|   main ();
|           ; var int local_14h @ rbp-0x14
|           ; var int local_10h @ rbp-0x10
|           ; var int local_ch @ rbp-0xc
|           ; var int local_8h @ rbp-0x8
|              ; DATA XREF from 0x0040087d (entry0)
|           0x00400b1e      55             push rbp
|           0x00400b1f      4889e5         mov rbp, rsp
|           0x00400b22      4883ec20       sub rsp, 0x20
|           0x00400b26      c745f4000000.  mov dword [local_ch], 0
|           0x00400b2d      c745f0000000.  mov dword [local_10h], 0
|           0x00400b34      c745ec000000.  mov dword [local_14h], 0
|           0x00400b3b      bed00c4000     mov esi, str.Enter_three_numbers__n ; 0x400cd0 ; "Enter three numbers!\n"
|           0x00400b40      bfa0216000     mov edi, obj.std::cout      ; 0x6021a0
|           0x00400b45      e8e6fcffff     call method.std::basic_ostream<char,std::char_traits<char>>&std::operator<<<std.char_traits<char>>(std::basic_ostream<char,std::char_traits<char>>&,charconst*)
|           0x00400b4a      488d45f4       lea rax, qword [local_ch]
|           0x00400b4e      4889c6         mov rsi, rax
|           0x00400b51      bf80206000     mov edi, obj.std::cin       ; 0x602080
|           0x00400b56      e8f5fcffff     call method.std::istream.operator>>(int&)
|           0x00400b5b      488d55f0       lea rdx, qword [local_10h]
|           0x00400b5f      4889d6         mov rsi, rdx
|           0x00400b62      4889c7         mov rdi, rax
|           0x00400b65      e8e6fcffff     call method.std::istream.operator>>(int&)
|           0x00400b6a      488d55ec       lea rdx, qword [local_14h]
|           0x00400b6e      4889d6         mov rsi, rdx
|           0x00400b71      4889c7         mov rdi, rax
|           0x00400b74      e8d7fcffff     call method.std::istream.operator>>(int&)
|           0x00400b79      8b55f4         mov edx, dword [local_ch]
|           0x00400b7c      8b45f0         mov eax, dword [local_10h]
|           0x00400b7f      01c2           add edx, eax
|           0x00400b81      8b45ec         mov eax, dword [local_14h]
|           0x00400b84      01d0           add eax, edx
|           0x00400b86      89c7           mov edi, eax
|           0x00400b88      e8c0fdffff     call sym.gen_int_
|           0x00400b8d      488945f8       mov qword [local_8h], rax
|           0x00400b91      8b55f4         mov edx, dword [local_ch]
|           0x00400b94      8b45f0         mov eax, dword [local_10h]
|           0x00400b97      01c2           add edx, eax
|           0x00400b99      8b45ec         mov eax, dword [local_14h]
|           0x00400b9c      01d0           add eax, edx
|           0x00400b9e      3d39050000     cmp eax, 0x539              ; 1337
|       ,=< 0x00400ba3      7527           jne 0x400bcc
|       |   0x00400ba5      bee60c4000     mov esi, str.easyctf_       ; 0x400ce6 ; "easyctf{"
|       |   0x00400baa      bfa0216000     mov edi, obj.std::cout      ; 0x6021a0
|       |   0x00400baf      e87cfcffff     call method.std::basic_ostream<char,std::char_traits<char>>&std::operator<<<std.char_traits<char>>(std::basic_ostream<char,std::char_traits<char>>&,charconst*)
|       |   0x00400bb4      488b45f8       mov rax, qword [local_8h]
|       |   0x00400bb8      4889c7         mov rdi, rax
|       |   0x00400bbb      e823ffffff     call sym.print_ptr_char__
|       |   0x00400bc0      bfef0c4000     mov edi, 0x400cef
|       |   0x00400bc5      e8f6fbffff     call sym.imp.puts           ; int puts(const char *s)
|      ,==< 0x00400bca      eb0f           jmp 0x400bdb
|      |`-> 0x00400bcc      bef10c4000     mov esi, str.nope._n        ; 0x400cf1 ; "nope.\n"
|      |    0x00400bd1      bfa0216000     mov edi, obj.std::cout      ; 0x6021a0
|      |    0x00400bd6      e855fcffff     call method.std::basic_ostream<char,std::char_traits<char>>&std::operator<<<std.char_traits<char>>(std::basic_ostream<char,std::char_traits<char>>&,charconst*)
|      |       ; JMP XREF from 0x00400bca (main)
|      `--> 0x00400bdb      488b45f8       mov rax, qword [local_8h]
|           0x00400bdf      4889c7         mov rdi, rax
|           0x00400be2      e859fcffff     call sym.imp.free           ; void free(void *ptr)
|           0x00400be7      b800000000     mov eax, 0
|           0x00400bec      c9             leave
\           0x00400bed      c3             ret
[0x00400860]> 
```
I have no idea how to read the assembly code, as well as the memory location in the system. However, from the output of running the program, with inputs that doesn't add up to the correct number, I believe that there is a conditional statement, somewhere in the source code that compares the addition of the 3 numbers, with the "correct" addition value. e.g.,

```sh
if num1 + num2 + num3 == X:		# X is the "correct" value
	print Flag
else:
	print "nope!" 
```

By looking at the r2 assembly output, it can be seen that there's ```cmp``` function that is followed by ```1337```. I believe that this is the correct summation value, since after that instruction, we can see ```jne 0x400bcc``` that may translate into "jump to location ```0x400bcc``` if not equal". This can be double checked, from the r2 output, where location ```0x400bcc``` contains the string "nope.\n". 

From the information at hand, i tried to run the program again, and it successfully gave me the flag.

```sh
❯ ./adder
Enter three numbers!
1337
0
0
easyctf{y0u_added_thr33_nums!}
```

## Flag
>easyctf{y0u_added_thr33_nums!}