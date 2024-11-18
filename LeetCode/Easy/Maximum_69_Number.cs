public class Solution {
    public int Maximum69Number(int num)
    {
        string strnum = num.ToString();
        int l = strnum.Length;
        string a = "";
        for (int i = 0; i < l; i++)
            a += "9";
        
        int b = int.Parse(a) - num;
        if (b == 0)
            return num;
        int ll = b.ToString().Length;
        int x = 1;
        for (int i = 0; i < (ll-1); i++)
            x *= 10;
        
        return num + (3 * x);
    }
}