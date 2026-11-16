# 十六条原三次来源：执行接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

原字段、源码及完整临时输入 pins 见同目录
\`2026-11-16-r150-original-sixteen-cubic-border-source-inputs-789f.json\`。
Python-flint 0.9.0；不需要网络或新原模型。所有大数组仅在临时目录。

## 第一步：真正的16个原右端

~~~sh
python 2026-11-16-r150-original-sixteen-cubic-border-constant-source-solve-789f.py \
  --leading-out LEADING_OUT --out CANDIDATE_OUT --seconds 180 --memory-mib 4096
~~~

实际首次 exit75：所有16个完整有理列已经先保存，但最终乘回没有完成。
不得把该回执当成功。原候选 checkpoint 与16文件全 SHA 是第二步输入。

## 第二步：只读完整原乘回

~~~sh
python 2026-11-16-r150-original-sixteen-cubic-border-integer-product-verification-789f.py \
  --leading-out LEADING_OUT --candidate-out CANDIDATE_OUT \
  --out VERIFIED_OUT --seconds 180 --memory-mib 4096
~~~

该版本严格绑定实际首次回执及候选 checkpoint；它不修改这些文件，不再运行 Dixon。
新环境重算时，候选数学内容应按完整 SHA 对照；若只因新执行用时而生成新回执，应记录新的执行身份并显式更新输入绑定，不能伪造旧回执或把相同文件名当同一数据。

验证先重建原有理105方块，再以每行/每列非零整数清分母，逐1680原坐标乘回。完成后写：
\`complete-verified-original-cubic-border-sources.json.gz\`
及 \`original-cubic-border-source-verification-receipt.json\`。

实际续验 exit0 / 24.702726178999秒。全部16字节及逻辑 SHA、全部35原输出、全部1680有理产品均真。最后模型仍明确
\`fullParameterBorderRemaindersComputed:false\`。

## 后继语义

原11条采用五个 \`du\` 与六个已付 \`NFdw\`，后者到原 \`dw\` 的完整五源校正仍须运输。全部常数属于原匹配域，参数不特化、不取倒数。后继全参数公式可以用精确算术表达式保存，但必须保留低次项、六条均值关系及非自由参数关系；不得称10维自由代数。
