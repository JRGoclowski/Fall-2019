#include <string>
#include <iostream>
#include <array>
using namespace std;

int FindWordsOfCount(int wordLength, string& strToSearch) {
	char punctuationArray[5] = { '.', ',', '!', '?', ' ' };
	auto eWCWalker = begin(punctuationArray);
	auto eWCEnd = end(punctuationArray);
	auto stringWalker = strToSearch.begin();
	auto stringEnd = strToSearch.end();
	int lengthCount = 0;
	int wordsFound = 0;
	while (stringWalker != stringEnd) {
		auto currentChar = *stringWalker;
		auto punctuationItr = find(eWCWalker, eWCEnd, currentChar);
		if (punctuationItr == eWCEnd) {
			lengthCount++;
		}
		else {
			if (lengthCount == wordLength) {
				wordsFound++;
			}
			lengthCount = 0;
		}
		stringWalker++;
	}
	return wordsFound;
}

int main() {
	string monoString = "Look, no one ever said Jotaro Kujo was a nice guy. I beat the crap outta people, more than I have to. Some are even still in the hospital. I've had idiot teachers who like to talk big, so I taught them a lesson, and they never came back to class. If I go to a restaurant and the food is bad, I make it a policy to stiff 'em with the bill. But, even a bastard like me... can spot true evil when he sees it! True evil, are those who use the weak for their own gain, then crush them underfoot when they're through! Especially an innocent woman! And that is exactly what you've done, isn't it? And your Stand gets to hide from the victim, the law, and the consequences. That's why... I will judge you myself! Two years ago, when I was inaugurated as the president of this country...there was a celebratory dinner held in the town I was born in. There, at that time, those present were treated to the meat of a freshly slaughtered lamb, an old custom passed down from a distant ancestor. The reality of this human world is that when we draw the curtain on a new age, there will be necessary trials for us to face. And in these trials...there are sure to be battles, and spilled blood. The more formidable the foe, the better the trial... These trials are 'offerings'...and the greater they are, the better. The Boomboom Family, Mountain Tim, Sandman, my wife, Wekapipo, Dio...that is what you all are. Polnareff, have you ever considered why humans wish to live? Humans live hoping to conquer their anxieties and fear, and attain peace of mind. Seeking fame, controlling others, and acquiring wealth are all done to achieve peace of mind. Marriage and friendship are also pursued as means of attaining peace of mind. When humans say they wish to help others, or that a thing is done for love or justice...it's all merely to give themselves peace of mind. To achieve peace of mind is the goal of all mankind. Now, given that, what anxiety could you possibly feel towards serving me? Any other peace of mind would come easily if you do. Doesn't challenging me, even knowing that it may spell your death, bring you anxiety? You are a very capable Stand user. It's a waste to kill you. Why not cut ties with Joestar and the others, and serve me for eternity? I can promise you peace of mind for eternity.";
	string easyTest = "This Sentence has words of varying lengths. They are over-emphasized numbers such as 4, 8, 3, 5, 2, 7, 7, 4, 3, 15, 7, 4, and 2";
	int targetLength = 3;
	int countCalled = FindWordsOfCount(targetLength, easyTest);
	cout << "Word length: " << targetLength << " \nAmount found: " << countCalled << endl;
}


