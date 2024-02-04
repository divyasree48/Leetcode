class Solution {
public:
    string minWindow(string s, string t) {
         map<char,int> mpp;
         int n1=s.size();
         int n2=t.size();
         for(int i=0;i<n2;i++){
             mpp[t[i]]++;
         }
         int c=0,i=0,j=0;
         int mini=INT_MAX;
         string res="";
         string s3="";
         while(j<n1){
            s3+=s[j];
            if(mpp.find(s[j])!=mpp.end()){
                if(mpp[s[j]]>0)
                c++;
                mpp[s[j]]--;
            }
            if(c==n2){
                while(mpp.find(s3[0])==mpp.end() or mpp[s3[0]]<0){
                    if(mpp.find(s3[0])!=mpp.end())
                    mpp[s3[0]]++;
                    i++;
                    s3.erase(s3.begin()+0);
                }
                //cout<<s3<<" ";
                if(mini>s3.size()){
                     mini=s3.size();
                     res=s3;
                     //cout<<res<<" "<<j;
                }
                mpp[s3[0]]++;
                s3.erase(s3.begin()+0);
                i++;
                c--;
            }
            j++;
         }
         return res;
    }
};