# 原 Bell 归一临界商的全局九生成元完整表示

作者：Astra-ISP-789f / normal_annihilator；与 /root 联合推导。AI-assisted: GPT-6 Astra Pro。2026-11-16。

## 1. 原完整理想及本次结论

沿用[全局匹配 Bell 双线性坐标](R150-appendix-global-matched-bell-hyperbolic-coordinates-and-normalized-critical-ideal.md)，记
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336),\quad
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\quad
S=B[u_0,\ldots,u_4],\quad b=y^{\mathsf T}w.
$$
全部17个原梯度经已付可逆多项式坐标运输后为
$$
F_i=\partial_{u_i}R'\ (0\le i<5),\qquad
W_j=\partial_{w_j}R',\quad Y_j=\partial_{y_j}R'\ (0\le j<6).
$$
原 Bell 非零归一支路对应完整理想
$$
I=(F_0,\ldots,F_4,W_0,\ldots,W_5,Y_0,\ldots,Y_5,b-1)\subset S.
$$
这里的坐标变换只除固定 $E$ 常数，保留原第三矩 Schur 来源和全部原梯度；没有倒置任何 $y,w$ 参数。

本次实际完成矩阵与全部原来源
$$
\mathcal Q:S^{57}\longrightarrow S^9,\qquad
\operatorname{coker}_S\mathcal Q\cong S/I.
\tag{1}
$$
所有矩阵条目对 $u$ 的次数至多1。在
$$
B_0=B/(b-1),\qquad S_0=B_0[u_0,\ldots,u_4]
$$
上，末列确为零；去掉该零列即得完整9×56表示
$$
\operatorname{coker}_{S_0}\mathcal Q_0\cong S_0/(F,W,Y).
\tag{2}
$$
这是全参数的单个表示，不需要把某条六维参数行补成可逆矩阵，也不需要另取开集。它没有断言原商为零或九个生成元自由。

## 2. 原十生成元表示与一个真正的单位关系

[完整原十生成元有限表示](R150-appendix-complete-original-ten-generator-finite-critical-presentation.md)已证明
$$
\operatorname{coker}_S\mathcal P_{57}\cong S/I
$$
并保存其57个原列和每列的18项原来源。十个普通单项式为
$$
m=(1,u_0,u_1,u_2,u_3,u_4,v_1,v_2,v_3,v_4),\qquad
(v_1,v_2,v_3,v_4)=(u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
记第6轴为 $e_*=e_{v_1}$，其他九轴集合为
$$
K=(0,1,2,3,4,5,7,8,9).
$$
原57列依次是50个边界列 $R_{i,a}=u_ie_a-N_ie_a$、六个完整 mean 列 $h_j$ 和
$$
R_{\mathrm{Bell}}=(b-1)e_0.
$$
这57列正是实际母68列中的编号0…49、61…67；11个被省去的矩梯度列已由原二次恒等式明确表示成边界列组合。

[完整六条 mean 关系](R150-appendix-complete-six-mean-relations-and-nine-bell-normalized-generators.md)给四个固定 $E$ 矩阵 $T_l$，使
$$
\bigl((h_j)_{v_l}\bigr)_{0\le j<6}=T_l y.
$$
本次从同一个原张量读取 $T_1$，重新构造其完整正则表示，精确求得并核验
$$
T_1T_1^{-1}=I_6,\qquad T_1^{-1}T_1=I_6
\quad\text{于 }E.
\tag{3}
$$
令
$$
\eta=w^{\mathsf T}T_1^{-1},\qquad r=\sum_{j=0}^5\eta_jh_j.
$$
则 $r$ 的所有系数属于 $B$，其第6系数由(3)严格等于
$$
r_*=w^{\mathsf T}T_1^{-1}T_1y=b.
\tag{4}
$$
不需要假定 $\eta$ 是可补全的参数行。

实际原字面边界路径为
$$
R_{1,u_4}=u_1e_{u_4}-e_{v_1},\qquad
R_{4,0}=u_4e_0-e_{u_4}.
$$
它们的原多项式来源均为零，所以
$$
R_{1,u_4}+u_1R_{4,0}=v_1e_0-e_*.
\tag{5}
$$
由(5)和原 Bell 列，得到完整的原57列组合
$$
\begin{aligned}
r_h
&=r+(b-1)(R_{1,u_4}+u_1R_{4,0})-v_1R_{\mathrm{Bell}}\\
&=r-(b-1)e_*\\
&=e_*+\sum_{a\in K}c_ae_a,\qquad c_a=r_a\in B.
\end{aligned}
\tag{6}
$$
因此 $r_h\in\operatorname{im}\mathcal P_{57}$，且被消去坐标的系数在原基环中就严格为1。没有使用 $b^{-1}$、任何 mean 参数的逆或一般位置假设。

## 3. 双向模同构及完整57列运输

定义
$$
P:S^{10}\longrightarrow S^9,\qquad
P(e_a)=\bar e_a\ (a\in K),\qquad
P(e_*)=-\sum_{a\in K}c_a\bar e_a.
$$
令 $\iota:S^9\to S^{10}$ 为保留原九轴的字面包含。直接有
$$
P\iota=I_9,\qquad
I_{10}-\iota P=r_he_*^{\mathsf T},\qquad
\ker P=Sr_h.
\tag{7}
$$
(6)说明该核已包含于原关系子模。故
$$
S^{10}/\operatorname{im}\mathcal P_{57}
\ \xrightarrow[\cong]{\,P\,}\
S^9/P(\operatorname{im}\mathcal P_{57}).
$$
取
$$
\mathcal Q=P\mathcal P_{57}
\tag{8}
$$
即证明(1)。其反向由 $\iota$ 给出；第二个(7)说明复合与恒等的差已在原关系子模中。

对每个原列 $p$，实际保存的完整新列是
$$
\mathcal Q_p=(\mathcal P_p)_K-c\,(\mathcal P_p)_*.
\tag{9}
$$
全部57列均保留，既不只取数值独立列，也不只取若干参数点。

$N_i,h_j,c,b-1$ 的条目都属于 $B$。原 $\mathcal P_{57}$ 仅边界列中的 $u_iI$ 含 $u$，所以(9)仍对 $u$ 至多一次。末Bell列在被删坐标上的系数为零，故其新列仍是
$$
(b-1)\bar e_0.
$$
这证明(2)去掉的是确切零列，不是未核的附加关系。完整性也不依赖于 $N_i$ 在自由十模上可交换；它来自原完整表示和(7)。

## 4. 全部原18来源

按原顺序记
$$
\mathcal G=(F_0,\ldots,F_4,W_0,\ldots,W_5,Y_0,\ldots,Y_5,b-1).
$$
母表示对每个原列 $p$ 保存
$$
m\,\mathcal P_p=\mathcal G\,s_p.
$$
由(5)的零来源及(6)，$r_h$ 的原来源准确为
$$
s_{r_h}=\sum_j\eta_js_{h_j}-v_1e_{\mathrm{Bell}}.
\tag{10}
$$
其中最后项是原 Bell−1 生成元的来源，不得省掉。新列对应原九个单项式 $m_K$，逐式有
$$
\begin{aligned}
m_K\mathcal Q_p
&=m\,\mathcal P_p-(\mathcal P_p)_*\,m r_h\\
&=\mathcal G\left(s_p-(\mathcal P_p)_*s_{r_h}\right).
\end{aligned}
\tag{11}
$$
因此实际保存的新来源是
$$
s'_p=s_p-(\mathcal P_p)_*s_{r_h}.
$$
总计513个矩阵坐标与1026个原来源坐标全部保留。由于(10)有 $-u_1u_4$，再乘原列的一次 $u$ 系数，来源的实际最大 $u$ 次数为3；矩阵的一次上界不意味着来源也一次。

(6)、(9)、(10)、(11)均以精确算术图保存，原参数叶继续引用已核原文件。本次全参数证明使用原母来源恒等式、完整精确常数逆和通用多项式代入。程序没有宣称对所有巨大参数多项式乘积再次完全展开。

## 5. 本次实际计算及可重现身份

实际 exit0，耗时12.36292547499761秒，最大常驻112848 KiB。其中固定 $E$ 单位块的 Dixon 求解耗时7.0993933040008415秒。完整候选在9.01402407099522秒先保存，两个方向的逆核验在12.150051719996554秒完成。

核验与实际输出包括：

- 全部324个原 $T_1$ 正则表示坐标；
- 行列整分母运输后的全部108个原有理右逆产品；
- 全部36个原 $E$ 左逆产品及原36个对称条目；
- 两个完整字面边界列、各自18个零来源、原Bell列；
- 全57列运输、513个新矩阵坐标、1026个原来源坐标；
- 所有新节点的来源编号、无前向引用和 $u$ 次数门。

母105774节点保持共享，只增加2889个节点。新原常数逆是追加的有 SHA 叶文件，不复制母原参数多项式，也不重解16条三次来源。

实际 binding：
~~~text
3299f05e3d9c2ea5f95b89c4fb8350b486b7b07d0a9ee01119c9ee235d14a0e5
~~~

| 临时对象 | 字节数 | SHA256 |
|---|---:|---|
| 实际小回执 | 2669 | 0a571570a0d472849407512fa61e60858f97eb62827c1769fe938da9fe6ae4e2 |
| 完整verified常逆 gzip | 3891224 | f2171b477163f0cbd3187496f12a1492d8f8c2112eb6752a3d21be181e59083a |
| 常逆逻辑内容 | 7836928 | 8d45309cf6b1d8aa8786427207ec5dbc90cd376c59917340b4c396475023cd7a |
| 共享算术扩展 gzip | 16680 | b5c45de7ee41247719de8585ddaf9734c5e8f0e7a89d9888addcfff95e7b8512 |
| 扩展逻辑内容 | 124152 | 4b7ea9e8b11cb641f59771c68471fd6b3570edddfbe2740e2deff3daf630ef81 |
| 完整9×57表示 gzip | 5029 | 200197e6c848590f5d7e7b61334cd2ccf4c07acdab60be6c1dac678767357270 |
| 表示逻辑内容 | 14862 | 7997d0ee10f5ec49fae9e9da998381550e787353238ac6357090dae85e747a74 |

可重现小文件：

- [实际源](../notes/2026-11-16-r150-original-global-nine-generator-critical-presentation-789f.py)；
- [原输入及源码 pins](../notes/2026-11-16-r150-original-global-nine-generator-critical-presentation-inputs-789f.json)；
- [执行与精确算术图接口](../notes/2026-11-16-r150-original-global-nine-generator-critical-presentation-interface-789f.md)；
- [实际执行身份](../notes/r150-nonrankone-execution-789f/20261116-local-original-global-nine-generator-critical-presentation.json)。

本结论在原三次域及其每个嵌入上成立，且在任意参数基变换后仍给同一个原商的 presentation。
此前[56个七生成元图册](R150-appendix-complete-original-fifty-six-seven-generator-critical-charts.md)仍可进一步局部化研究；本次无需使用那些子式开集。全 Bell 非零临界商是否为零仍是待证问题。
