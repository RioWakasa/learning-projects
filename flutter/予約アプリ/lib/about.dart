import 'package:flutter/material.dart';

class AboutPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('About us',
        style:TextStyle(
          fontWeight: FontWeight.bold,
        )),
      ),
      body: SingleChildScrollView(  
        padding: const EdgeInsets.all(20.0),
        child: Column(children: [
          Container(
            height: 100,
            width: 100,
            child: Image.asset('images/sample.png',
            fit: BoxFit.contain,),  
            ),
          const Text('いらっしゃいませ、サンプルフードへようこそ！\n私たちは夢と美味しさが交わる場所を提供し、お客様に心地よい時間をお過ごしいただくことをお約束します。',
          textAlign: TextAlign.center,),
          Container(
            padding: const EdgeInsets.all(10.0),
            child: const Text('私たちの物語',
            style: TextStyle(
              fontSize: 20,
              color: Color.fromARGB(255, 255, 123, 0),
              fontWeight: FontWeight.bold,
            )),
          ),
          const Text('サンプルフードは、夢想家で料理の魔法使い、エリアンナ・サンドウィングによって設立されました。エリアンナは、異世界の風景や夢の中で出会った美味しい料理に魅了され、その魔法を現実のカフェにもたらそうという夢を抱いていました。彼女は、異次元の食材や秘密のレシピを集め、心を込めて創り上げた料理でカフェを満たしました。サンプルフードは、まるで夢の中にいるかのような雰囲気を提供し、お客様に魔法のようなひとときを提供します。'),
          Container(
            padding: const EdgeInsets.all(10.0),
            child: const Text('私たちの理念',
            style: TextStyle(
              fontSize: 20,
              color: Color.fromARGB(255, 255, 123, 0),
              fontWeight: FontWeight.bold,
            )),
          ),
          const Text('私たちは、お客様に心から喜んでいただける食事とくつろぎの空間を提供することに誇りを持っています。料理は私たちのアートであり、お客様は私たちの共演者です。サンプルフードは、単なる食事の場所ではなく、夢や魔法を感じることのできる特別な場所として位置づけています。'),
          Container(
            padding: const EdgeInsets.all(10.0),
            child: const Text('私たちのメニュー',
            style: TextStyle(
              fontSize: 20,
              color: Color.fromARGB(255, 255, 123, 0),
              fontWeight: FontWeight.bold,
            )),
          ),
          const Text('私たちのメニューは、エリアンナが世界中から集めた異次元の食材と、彼女の創造力によって生み出された特別な料理で構成されています。シュールで美しいデザート、夢幻的なドリンク、そして心温まるランチセットまで、幅広い選択肢をご用意しています。'),
          Container(
            padding: const EdgeInsets.all(10.0),
            child: const Text('お問い合わせ',
            style: TextStyle(
              fontSize: 20,
              color: Color.fromARGB(255, 255, 123, 0),
              fontWeight: FontWeight.bold,
            )),
          ),
          const Text('ご質問やご要望がありましたら、どうぞお気軽にお知らせください。私たちはいつもお客様の声に耳を傾け、より良い体験を提供できるよう努めています。\nサンプルフードで、夢と美味しさの旅に出かけませんか？\n夢を味わい、美味しいひとときを共有しましょう。\n心よりお待ちしております。'),
          const Text('エリアンナ・サンドウィング\nサンプルフード オーナー',
          textAlign: TextAlign.start,
          style: TextStyle(
            fontSize: 10,
          )),
        ]
        ),
      ),
    );
  }
}