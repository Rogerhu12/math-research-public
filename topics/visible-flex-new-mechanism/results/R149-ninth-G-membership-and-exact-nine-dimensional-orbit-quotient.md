# R149：第九次 G 平移的完整原式成员，商轨道恰九维

日期：2026-11-15。**已证明；G平移链至此结束，不再派下一阶。**

记 $R=\mathcal R_8$、$U=\mathcal U_4$、$A_G=R+\operatorname{span}\operatorname{Orb}(G)$。
第九次同右锚平移的两个完整模式满足同一原有理恒等式

$$
\boxed{N^9G=-5670\,\mathcal B_{r_0}(W_{19})\in R.}
\tag{1}
$$

这里 $W_{19}$ 指已发表v2的**原索引19**，不是其他导出中重排后的列号。
结合 [R147](R147-eighth-G-translation-and-237-query-control.md) 及所有前驱，

$$
\boxed{\dim(A_G/R)=9,\qquad
\{[G],[NG],\ldots,[N^8G]\}\text{ 是该商的一组基。}}
\tag{2}
$$

这只是已知可调子空间的商结构。R136已证明J在整个 $A_G$ 外，故 $U\ne A_G$；
本稿不会把这条已完成的链误作完整第四成本或主课题完成。

## 1. 公开实际与原目标

[公开 run 43657083833](https://github.com/Rogerhu12/math-research-public/actions/runs/43657083833)，
source `daf7ef26ec86097ace56ac806e88059a98f7bf9e`，lane `g_translation_successor`，
显式 order9。生产器仍为39670 B的
[literature_G_translation_successor.py](../scripts/literature_G_translation_successor.py)，SHA256
`a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406`。
紧前G8的全部来源与两模式原目标均绑定，相同19项人工开发结果复用。

实际 complete，耗时 **4.466764426000005 秒**，峰值 RSS **125.0859375 MiB**。
只新构造真权−8的两个完整响应列，没有重算以前权块、forcing或W模板。

| 模式 | $N^9G$ 原项数 | 原式 SHA256 |
|---|---:|---|
| −4 | 2 | `db405e12f047cdfef445e0e8f9f4ba5ab7b032984a6c3d80b782149a0d039956` |
| −2 | 6 | `f328972790ba8b62c18c759a5ed13522052870e54d2241a4dd5386fad6f18ddd` |

仍使用 $N\xi=1,Nq^{(j)}=N\bar q^{(j)}=0,N(IF)=I(NF)$，保持共同右锚。
N是输入和查询共同仿射输运的生成元，不是固定profile的完整 $\xi$ 导数。

## 2. 两模式共用的准确响应表示

新权块的原列0、1分别为 $\mathcal B_{r_0}(W_{18})$、$\mathcal B_{r_0}(W_{19})$。
二次坐标索引均为3，名称r0。第二列的原第三模板身份为

~~~text
cdd32759064ac990ad45a67b3c63da2bd64813059ae62b23c0d7f7b9250cd3f1
~~~

其完整pure根原本就是零；mixed原根 SHA256 为
`6f822be2b064bbad6a39dad364c941aff84b83049cf1530366cf70d55beb083e`。
不能据pure为零删去mixed列。

消费器找到唯一所用系数列表 `[[1,"-5670"]]` 后，分别从两个模式的原式重新形成

$$\Delta_m=(N^9G)_m+5670(\mathcal B_{r_0}(W_{19}))_m,\qquad m=-4,-2.$$

两条差式都经准确、保持同一右锚的sound身份化为零。原差哈希为

| 模式 | 原差 SHA256 |
|---|---|
| −4 | `db405e12f047cdfef445e0e8f9f4ba5ab7b032984a6c3d80b782149a0d039956` |
| −2 | `1355cc1314087133ccc57bb97f2a9170b255b486f43eb818f663c7037a810ac9` |

两模式验证零的规范 SHA256 均为
`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。
这是从原函数得到的阳性恒等式，不需要假设归约完备，也不靠模素数或有限profile样本。
同一个实系数−5670用于两模式，包含原完整相位归一化，不再外乘相位因子。

## 3. 为何准确确定商轨道维数

前驱已分别证明 $G,NG,\ldots,N^8G$ 不属于R，且其真缩放权依次为
$1,0,-1,\ldots,-7$。R是真缩放不变子空间，有限真实函数空间的不同权直和，
故这些九个商类线性独立。

式(1)给第九个平移后继属于R。R又在N下不变，所以所有更高平移后继都在R。
G本身真权1，正缩放不会生成独立的新种子；全部仿射轨道模R因此由前九类张成。
这同时给(2)的上下界。原 $N^{10}G=0$ 结构上界也仍成立，但无需再跑一次零目标。

在商空间上，N对这组基恰形成一个长为9的幂零链：末项 $[N^8G]$ 非零，
再作用N即为零。不要把(2)误写成未取模的原轨道本身只有9维；式(1)的响应项
在未取商的空间中仍须保留。

本次新权块只给两个原列和真实维数上界2，没有为这两个列另作原有理独立性证明，
故不从两个非零word代表增加R的维数下界。R147已付的
$\dim R\ge228$、$\dim A_G\ge237$、$\dim U\ge238$继续有效。
R120、R122的lineality和至少237个真实共同查询也继续有效，J仍不算新增有符号控制。

## 4. 完整证据与后继任务

目录 `notes/actions-43657083833-1-g_translation_successor`。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43657083833-1-g_translation_successor/G-ninth-translation.json) | 15373 | `58112411bb88c644806338fa283147128443a192be7e71ef17c6194c125f9e44` |
| [完整数学报告](../notes/actions-43657083833-1-g_translation_successor/G-ninth-translation-complete-report.json.gz) | 7011 | `3f07e355a91cd69105fee3ace1c9ed6658d6e799a4c3811464a700a1c382e2e6` |
| [全部新原式](../notes/actions-43657083833-1-g_translation_successor/G-ninth-translation-original-expressions.json.gz) | 3346 | `f0532253443d3a3b22ae054798db3c548275ae8285c605767d4e5cc0a7c0e76b` |
| [发布回执](../notes/actions-43657083833-1-g_translation_successor/receipt.json) | 35426 | `ebbae5204a1e774c5f344d3944035337b66685e015d4e849cd1dcd221d8fa9ba` |

数学原文24344 B，SHA256
`e4375bb74294e3a411533a9ec9b6a9a0dcdb55f7c8e8143ccd3a7bd3003a35e6`。
新原式原文9237 B，SHA256
`1f45c6a4f850c5887021ed9aa7d9b90bf4ccdd3bcde89ca641e32b2a80729838`；
保存全部6原根、39 atoms、57根单项。

G链结束后，立即接open中的真正剩余问题：R148的完整h轴系数D0及其与J的关系、
J的一般pure对完整已发表响应像的成员门，以及同g几何目标阶梯。
完整action、ruling、高阶收敛、闭嵌入、全时reach和宏观连续等距族仍未完成。
