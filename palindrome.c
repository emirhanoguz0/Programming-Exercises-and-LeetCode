bool isPalindrome(int x) {

    if(x<0){
        return false;
    }

    long n = x, k=0,y=0;

    while(x > 0){

        k = x % 10;
        y = y*10 + k;
        x /= 10;

    }

    if (n==y){
        return true;
    }
    return false;
}