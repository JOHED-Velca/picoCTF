# picoCTF 
# The beginners guide to picoGym - SOLUTION

1. Obedient cat: wget [url], cat flag | xclip -selection clipboard.
	wget https://mercury.picoctf.net/static/a5683698ac318b47bd060cb78685
	9f23/flag && cat flag | xclip -selection clipboard
	FLAG: picoCTF{s4n1ty_v3r1f13d_4a2b35fd}
2. Super SSH: ssh ctf-player@titan.picoctf.net -p 54763 | input: password.

3. What is netcat: netcat jupiter.challenges.picoctf.org 41120.

4. Decode ROT13: echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}" 
	| tr 'A-Za-z' 'N-ZA-Mn-za-m'
	python3 -c 'import codecs; print(codecs.encode("cvpbPGS{arkg_gvzr_V\'
	yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}", "rot13"))'

5.Warmed Up:
	a. printf "%d\n" 0x3D
	b. echo "ibase=16; 3D" | bc
	c. python3 -c 'print(int("3D", 16))'

6. 2Warm:
	a. echo "obase=2; 42" | bc
	b. python3 -c 'print(bin(42)[2:])'
	c. echo "2 o 42 p" | dc

7. Bases:
	a. echo "bDNhcm5fdGgzX3IwcDM1" | base64 --decode
	b. python3 -c 'import base64; print(base64.b64decode(
	"bDNhcm5fdGgzX3IwcDM1").decode())'

8. Wave a flag:
	wget [url]
	/warm -h
	FLAG: picoCTF{b1scu1ts_4nd_gr4vy_30e77291}

9. Tab, Tab, Attack:
	wget [url]
	unzip [file]
	cd Ad[tab][tab]...

10. Inspector:
	Flag is divided in 3 parts and you can find 1/3 of it in the
	HTML, .css, .js files.

11. Strings it:
	strings strings | grep -i "picoCTF"  // -i for case sensitive
	FLAG:picoCTF{5tRIng5_1T_d66c7bb7}

12. First Grep:
	strings file | grep "pico"
	FLAG: picoCTF{grep_is_good_to_find_things_5af9d829}

13. Where are the robots:
	a. add "/robotos.txt" to the webpage url.
	b. use the new info to add it to the url instead of the "/robots.txt"
	like this: https://url//477ce.html
	FLAG: picoCTF{ca1cu1at1ng_Mach1n3s_477ce}

14. Python Wrangling:
	cat pw.txt | xclip -selection clipboard
	python3 ende.py -d flag.txt.en
	[paste the password]
	FLAG: picoCTF{4p0110_1n_7h3_h0us3_6008014f}

15. PW Crack 1:
	a. wget [programURL] && wget [flagURL]
	b. Analize the code to find the password
	c. python3 level1.py
	FLAG: picoCTF{545h_r1ng1ng_1b2fd683}

16. PW Crack 2:
	a. wget [URLs]
	b. python3 level2.py, password:39ce
	FLAG: picoCTF{tr45h_51ng1ng_502ec42e}

17. PW Crack 3:
	a. Manually try every password to find the correct one (3rd).
	b. Modify the last function to loop through the array of options:
	def level_3_pw_check():
    		pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
    		for pw in pos_pw_list:
        		user_pw_hash = hash_pw(pw)

        		if( user_pw_hash == correct_pw_hash ):
            			print("Welcome back... your flag, user:")
            			decryption = str_xor(flag_enc.decode(), pw)
            			print(decryption)
            			return
        		print("That password is incorrect")

	FLAG: picoCTF{m45h_fl1ng1ng_cd6ed2eb}

18. PW Crack 4: Change the last function and include a for loop.
def level_4_pw_check():
    pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]
    for pw in pos_pw_list:
        user_pw_hash = hash_pw(pw)

        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), pw)
            print(decryption)
            return
        print("That password is incorrect")

	FLAG: picoCTF{fl45h_5pr1ng1ng_d770d48c}

19. PW Crack 5: Modify last function.
	def level_5_pw_check():
    	f = open('dictionary.txt', 'r')
    	while True:
        	user_pw = (f.read(5).strip())
        	user_pw_hash = hash_pw(user_pw)
        	if( user_pw_hash == correct_pw_hash ):
            		print("Welcome back... your flag, user:")
            		decryption = str_xor(flag_enc.decode(), user_pw)
            		print(decryption)
            		return
    	print("That password is incorrect")
	
	FLAG:picoCTF{h45h_sl1ng1ng_36e992a6}

20. Emhance!: Analize the content of the image with vim, nano or cat.
	cat drawing.flag.svg | grep "</tspan>"
	FLAG: picoCTF{3nh4nc3d_24374675}

21. Big Zip: grep -r 'picoCTF*' *
	FLAG: picoCTF{gr3p_15_m4g1c_ef8790dc}

22. Vault-door-training:
	vim [sourceCode]
	FLAG: picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}

23. Keygenme-py: Analize the code, realize that we need to convert the username to 
	sha256 hash (In this case the username is "FREEMAN").
	Use an online calculator for accuracy.

	FLAG: picoCTF{1n_7h3_|<3y_of_0d208392}

24. Buffer Overflow 0:	
