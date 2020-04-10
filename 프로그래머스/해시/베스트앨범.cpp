#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b){
    if(a.second == b.second)
        return a.first < b.first;
    else
        return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> summap; // key : 장르, value : 장르 재생횟수
    unordered_map<string, vector<pair<int, int> > > genmap; // key : 장르, value : (고유번호, 곡 재생횟수)를 담는 벡터
    
    for(int i = 0; i < genres.size(); i++){
        summap[genres[i]] += plays[i];
        genmap[genres[i]].push_back(make_pair(i, plays[i]));
    }

    //장르 재생횟수 순 정렬 오름차순
    vector<pair<int, string> > summapV;
    for(auto pair : summap)
        summapV.push_back(make_pair(pair.second, pair.first));
    sort(summapV.begin(), summapV.end());
    
    for(int i = summapV.size()-1; i >= 0; i--){ //내림차순 접근
        //vector<pair<int, int> > v = genmap[summapV[i].second];
        sort(genmap[summapV[i].second].begin(), genmap[summapV[i].second].end(), compare);
        
          for(int j = 0; j < genmap[summapV[i].second].size() && j < 2; j++)
            answer.push_back(genmap[summapV[i].second][j].first);
    }
    
    return answer;
}
