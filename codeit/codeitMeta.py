def template_cp():
    template = """ /*
    author: @alphaX86
    created using: https://gist.github.com/alphaX86/ad925deb146b66f7ab3149318adb4fb0
*/
    /* For better understanding of this code, you may need 3 files: source.cpp, input.txt, output.txt */

    #include <bits/stdc++.h> 
    //Include libraries accordingly

    using namespace std; 

    int main() 
    { 
        ios_base::sync_with_stdio(false); 
        cin.tie(NULL); 

    /* This is needed as most contests use this format */
    #ifndef ONLINE_JUDGE  
        freopen("input.txt", "r", stdin); 
        freopen("error.txt", "w", stderr); 
        freopen("output.txt", "w", stdout); 
        //If you do not need error txt, remove it accordingly
    #endif 

        int t = 1; 
        /*is Single Test case?*/ 
        cin >> t; 
        while (t--) { 
            //Code here
            cout << endl; 
        } 

        cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; //Optional
        return 0; 
    } """

    return template

def get_filename():
    fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
    return fileNames

def get_fn_beginner():
    fileNames = ['A.cpp','B.cpp','C.cpp']
    return fileNames