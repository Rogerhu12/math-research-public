# R186：权 −2 的完整原函数核与真正五维字符头部

日期：2026-11-15。**已证明；完整公开精确续算，配 R159、R163、R178、R179 的原函数定理。**

R163 真权 $-2$ 完整十四族的 77 个字面基列，现在全部完成共同规范 word 比较。真实函数 rank 是 **52**，完整函数核有 **25** 个三角基关系；与 R174 已付的 70 条字面关系合并，给原 147 列的 **95 维完整原函数核**。

三个不同的空间具有准确维数：

$$
\boxed{
\dim U_{-2}=52,\qquad
\dim(U_{-2}/R_{-2})=12,\qquad
\dim\mathcal H_{-2}=5,
}
\qquad
\mathcal H_{-2}=\frac{U_{-2}}{R_{-2}+\mathsf N U_{-1}}.           \tag{1}
$$

五维现在是**完整真实字符头部**，不再是只含必要条件的外空间。任意五个实参数都定义一个该头部上的真实线性泛函；哪些泛函对全部真实成本非负，仍是另外的全 action 问题。

完整五参数形状还给出一个即时后果：由 R175 的最高层锐利判据，任何正字符都必须令其中一个参数 $m$ 为零。下文给出剩余四参数完整 action，不把最高层必要条件冒作全层正性。

## 1. 原列和续算范围

沿 [R174](R174-nine-original-character-relations-and-rejection-of-the-positive-outer-point.md)、
[R182](R182-shared-word-original-identity-rejects-the-all-layer-positive-point.md)，记

$$
(C_0,\ldots,C_{146})
=(R_0,\ldots,R_{39},V_0,\ldots,V_{106}).                         \tag{2}
$$

$R_j$ 是已发完整该权响应基，$V_i$ 是 R163 head 中 107 个 normal 原记录。R174 的 70 条原式字面身份把它们准确归到 77 列，本次不重新产生旧身份。

公开续算为 run **43676765171**，source

**ca4e52869123fa97df4560232a03f9529cf05332**，

lane **character_head_word_relations**。它读取 R182 已发完整状态，从 cursor 62 继续至 77，使用同一 driver、同一固定颜色模块、同六份原输入和同一个 R177 指定点。

恢复回执明确记录：旧 original normalization 重放数为 0，旧 elimination pivot 重放数为 0，恢复 62 个已成列且无未完成子阶段，没有派生缓存压缩。已过的 atom 接口两项人工严格复用，没有再次运行。

本次没有新的 profile 评价、幂尾代入、LP、路径积分、旧 RREF 或原 forcing/响应编译。

## 2. 共同规范表给出完整真实函数核

所有原式保持同一物理右锚

$$
I(F)(\xi)=\int_r^\xi F,
$$

输入颜色及相应 jets 在共同右 collar 上为零。每列的两个忠实分量是

$$
\pi C=C_{-4},\qquad \Xi C=[q^2\bar q^2]C_{-2}.                  \tag{3}
$$

完整证书保存 **154** 份分量转换。42 份为已有 pure 原身份——R40 的 40 份及已付的 J、轴 $D_0$ 各一份；112 份由 R178 新固定颜色映射得到。154 份全部绑定原根 hash、同一右锚和转换来源，并通过固定余 letter 语法检查。

[R178](R178-fixed-color-priority-IBP-and-terminating-shared-word-map.md) 保证转换是原函数身份；[R179](R179-universal-independence-of-fixed-color-remainder-words.md) 保证该规范 word 字典普适函数单射。故原列组合若为零，其两个分量的规范表也必为零。反向，两个规范表为零先给 pure 身份，再由 [R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 给完整 canonical 身份。因此

$$
\boxed{
\ker(\text{77 列共同规范矩阵})
=\ker(\text{77 列完整原函数评价}).
}                                                               \tag{4}
$$

证明不把 primitive 独立赋值，也不使用固定 profile 的偶然等式。旧 pure 代表的执行路径无需与新映射相同；同锚 sound 身份和规范语法已经由 R179 给出表示唯一性。

### 2.1 52 个真基列和 R40 独立性

完整证书的 shared_representative_matrix_basis_columns 精确为

$$
0,1,\ldots,39,\quad
40,41,42,43,44,45,46,49,51,52,54,58.                            \tag{5}
$$

这是 **77 字面基内部的下标**。首 40 列全部是原 R40，共同规范矩阵已经把它们全部保为独立列。由 (4)，这是原函数独立，绝非仅从 R174 的字面独立推断；也与 [R131](R131-third-G-translation-separation-and-111-query-control.md) 已发该权真实 R40 基证明一致。

另外十二列的 normal 下标为

$$
0,1,2,4,5,7,8,23,28,30,38,46.                                 \tag{6}
$$

它们模 R 的类给 $U_{-2}/R_{-2}$ 的真基。R163 的完整张成定理 $U_{-2}=R_{-2}+T_{-2}$ 把这些十四族的全部 107 原记录和 R40 接到完整 $U_{-2}$，不是只接到一个选定子空间。故 (5)–(6) 证明 (1) 的前两个维数。

### 2.2 原 147 列的 95 维完整核

25 条新关系的依赖 77 列下标为

$$
\begin{aligned}
&47,48,50,53,55,56,57,59,60,61,62,63,64,65,66,67,68,\\
&69,70,71,72,73,74,75,76.
\end{aligned}                                                  \tag{7}
$$

每条只用自身及先前列，自身系数为正、非零。这些关系构成 $77-52=25$ 维完整三角核。每条另保存完整 $-4,-2$ 原多项式差、所有支持列的绑定转换和两个忠实规范表的独立零和，不只保存消元余式。

R174 的旧 70 条字面身份先消去另外 70 个原列；(7) 再消去其中 25 列。任意 147 列真实关系最终归到 (5) 的 52 个真独立列，因此无剩余关系。两组三角关系的主列互不相同，合计给

$$
\boxed{\dim\ker(C_0,\ldots,C_{146})=70+25=95.}                    \tag{8}
$$

完整证书保留新 25 条关系的 dense77、dense147、稀疏原系数以及两模式原差；旧 70 条没有重算。

## 3. 七条新增字符等式

继续使用原 $\nu=By$，不重做其 RREF。$y_0,\ldots,y_{22}$ 的自由 normal 下标仍是

$$
(2,3,14,23,26,28,38,43,58,63,67,69,73,90,91,94,96,97,
99,100,101,103,104).                                          \tag{9}
$$

25 条函数核关系中，七条在旧 B、R168、R174 和此前新行之外给新独立等式，其 relation_index 为

$$
9,10,17,18,20,22,24.                                         \tag{10}
$$

证书保存的**未缩放旧 free 行**是

$$
\begin{aligned}
q_9={}&768y_0+256y_1+256y_2+256y_8-768y_{12},\\
q_{10}={}&-880201728y_0-434294784y_1-434294784y_2
-81285120y_3-272056320y_5\\
&+34836480y_6+104509440y_9+891813888y_{12},\\
q_{17}={}&2761371648y_0+1270370304y_1+1270370304y_2
+499322880y_3+272056320y_5\\
&+174182400y_6-2563964928y_{12}+418037760y_{13},\\
q_{18}={}&-3096576y_0-1548288y_1-1548288y_2
+552960y_5+3096576y_{12}+774144y_{14},\\
q_{20}={}&516096y_0+258048y_1+258048y_2
-847872y_5-516096y_{12}+774144y_{17},\\
q_{22}={}&-51093504y_0-25546752y_1-25546752y_2
-27537408y_5+51093504y_{12}+27869184y_{19},\\
q_{24}={}&-2582212608y_0-1210650624y_1-1210650624y_2
-499322880y_3-272056320y_5\\
&-174182400y_6+2444525568y_{12}+179159040y_{21}.
\end{aligned}                                                 \tag{11}
$$

全部等于零。已发状态逐次约去旧行后的 pivot 依次是

$$
2,\ 3,\ 6,\ 11,\ 19,\ 20,\ 8,                                 \tag{12}
$$

彼此不同，且不在旧 R168/R174 的 pivot 中。其余 18 条新函数核关系在此字符坐标中约化为零，但仍属于完整函数核基，不可从 (8) 中省掉。

### 3.1 R174 十二参数中的简明形式

沿 R174 记

$$
\begin{aligned}
a_{\rm static}(k)&=(1+k^2)(\alpha+\beta k^2),\\
b_0(k)&=B_0+B_2k^2,\qquad b_1(k)=C_1k-4B_2k^3,\\
b_2(k)&=D_0+D_2k^2+4B_2k^4.
\end{aligned}
$$

最高层十数为 $(a,b,c,d,e,f,g,j,\ell,m)$，并已满足 R174 的五条最高层原式关系。置 $\delta=D_2$，在这些继承条件下，(11) 等价于

$$
\boxed{
\begin{aligned}
&D_0+\alpha+\beta=0,\\
&7B_0-3C_1-9\delta+2\alpha+\beta+\frac{164}{7}B_2=0,\\
&43B_0+15C_1+36a+2\alpha+19\beta+\frac{164}{7}B_2=0,\\
&5B_2+7b=0,\qquad 23B_2-21e=0,\qquad 83B_2-84g=0,\\
&\beta+7a+3\ell=0.
\end{aligned}}                                                \tag{13}
$$

最后一式是 $q_{17}+q_{24}$ 除以 59719680；其余是对应行在已付条件下的非零有理缩放。这是读取已发表精确行后的纸面重排，没有本地研究消元。

## 4. 为什么是完整真实的五维头部

原 finite certificate 的 124 条精确等式 rank 为 84，给 $\nu=By$ 的 23 个自由坐标。其源码直接把 head_translation_presentation 的**全部 66 个** R163 平移分母生成式加入等式，不是只检查零标签或部分匹配。

再加 R168 的两个独立行、R174 的九个独立行和本次七个独立行，剩余维数为

$$
107-(84+2+9+7)=5.                                             \tag{14}
$$

本次完整状态保存的五个最终 free 位置为

$$
(9,12,13,21,22).                                             \tag{15}
$$

需要同时证明两个方向，才能把 (14) 读作真正的 $\mathcal H_{-2}$ 维数。

**必要性。** 每个真实权 $-2$ 平移不变字符杀 $R_{-2}$，满足完整原函数核、R163 全部平移生成关系，以及已证 R164 第 7–8、10 节的协变和 R168 奇偶关系。R164 第 7 节的 Lie cocycle 身份及第 10 节明确覆盖尚未假设正性的真实字符；finite 的 static/PSD/path 半空间位于独立 ineq，不属于这里计数的等式 B。因此其 107 个值属于 (14) 的解空间。

**充分性。** 任取该解，给 $R_j$ 值零、$V_i$ 值 $\nu_i$。旧 70 条字面核加新 25 条函数核已完整，解杀全部 95 条关系，所以赋值在真正的 $U_{-2}$ 上定义良好。旧 66 个 D 行又给 $\lambda D_{-2}=0$。R163 的精确身份

$$
R_{-2}+\mathsf N U_{-1}=R_{-2}+D_{-2}
$$

使它因子化到 $\mathcal H_{-2}$。在其余真权上置零后，它就是整个 U 上权 $-2$ 的真实仿射字符。此方向不要求正性。

所以该五维解空间与 $\mathcal H_{-2}^*$ 双向对应，证明 (1) 的第三个维数，并给

$$
\dim\frac{R_{-2}+\mathsf N U_{-1}}{R_{-2}}=7,\qquad
\dim(R_{-2}+\mathsf N U_{-1})=47.                              \tag{16}
$$

这里的 7 是平移分母在真十二维 $U_{-2}/R_{-2}$ 中的维数，由完整对偶对应推得；不是把“七条新增 word 行”直接当成七个函数向量独立。

## 5. 全部真实字符的五参数完整形状

取自由参数

$$
\boxed{(\alpha,\beta,a,\delta,m)\in\mathbb R^5.}                 \tag{17}
$$

它们与 (15) 的转换为

$$
y_9=\delta,\quad y_{12}=-\alpha,\quad y_{13}=a,\quad
y_{21}=-\frac{7a+\beta}{3},\quad y_{22}=m,                      \tag{18}
$$

可逆。因此每个实五元组都定义真实字符；这一步与 R177 那类尚未良定义的外点已经不同。

静态、二次与最高层系数准确为

$$
\boxed{
\begin{aligned}
&a_{\rm static}(k)=(1+k^2)(\alpha+\beta k^2),\\
&\ell=-\frac{7a+\beta}{3},\qquad D_0=-\alpha-\beta,\qquad
D_2=\delta,\qquad B_2=\frac{7m}{4},\\
&B_0=\frac{15\delta-4\alpha-8\beta-12a-82m}{26},\\
&C_1=\frac{8\alpha-10\beta-28a+164m-43\delta}{26},\\
&(b,c,d,e,f,g,j)
=\left(-\frac{5m}{4},\frac{5m}{4},-\frac{5m}{16},
\frac{23m}{12},-\frac{13m}{24},\frac{83m}{48},-\frac{25m}{6}\right).
\end{aligned}}                                                \tag{19}
$$

$b_0,b_1,b_2$ 仍用 §3.1 的完整多项式。最高十数是 $(a,b,c,d,e,f,g,j,\ell,m)$，包含 H 的两个系数 $e,f$。

同一八矩乘子由 R164 给出，按 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$ 顺序为

$$
\boxed{\mu=(0,\,2\alpha,\,4(\alpha+\beta),\,0,\,0,\,0,\,0,\,8\alpha).}
                                                                    \tag{20}
$$

这是规范化后 $\mathscr L$ 的乘子；恢复原 L 时仍须加回同一 $\widetilde\lambda\Gamma$。没有混用八参考状态编号与 E8 坐标编号。

头部中的五个类

$$
[V_0],\quad[V_2],\quad[V_{90}],\quad[V_{63}],\quad[V_{104}]        \tag{21}
$$

给一个真基：其在任意字符上的值依次为 $\alpha,\beta,a,\delta,m$，而 (17)–(18) 允许这些值任意独立指定。

## 6. 完整最高层迫正字符 m=0

[R175](R175-complete-highest-action-sharp-two-by-two-criterion-after-original-relations.md) 给完整最高层的锐利条件

$$
a\ge0,\qquad\ell+\frac{25a}{9}\ge0,\qquad
M=\begin{pmatrix}b/4&3b/4+3f/2\\
3b/4+3f/2&23b/12+2f+g\end{pmatrix}\succeq0.                    \tag{22}
$$

真实正字符必须满足它；三个时长层的分离和真实补偿已由既有定理支付。代入 (19) 得

$$
M=m\begin{pmatrix}-5/16&-7/4\\-7/4&-7/4\end{pmatrix},
\qquad
\det M=-\frac{161}{64}m^2.                                    \tag{23}
$$

所以

$$
\boxed{\lambda\text{ 为真实正字符}\ \Longrightarrow\ m=0.}       \tag{24}
$$

这同时令 $b,c,d,e,f,g,j,B_2$ 为零。完整最高层不再含 $k'$ 或 $k''$；它是全部真实函数关系和全最高层判据的后果，没有从某条 A 系数零就猜测 H/Q4 消失。

静态及最高层的剩余必要条件为

$$
\boxed{\alpha\ge0,\qquad a\ge0,\qquad 0\le\beta\le\frac{4a}{3}.} \tag{25}
$$

其中 $\ell+25a/9=(4a-3\beta)/9$。这尚未完成整个 action 的正性分类。

### 6.1 剩余四参数的完整 action

令 $r=\log h$、$v=r'$，保真实水平关系 $\omega'=k'/(2h)$。当 $m=0$ 时，R164 的规范化并扣同一乘子的完整 action 是

$$
\boxed{
\begin{aligned}
\mathcal I_{\alpha,\beta,a,\delta}[r,k]
=\int e^{-2r}\bigg\{&
a(v'+v^2)^2-\frac{7a+\beta}{3}v^4\\
&+B_0(k')^2+C_1kvk'
+(-\alpha-\beta+\delta k^2)v^2\\
&+(1+k^2)(\alpha+\beta k^2)
\bigg\}\,ds,
\end{aligned}}                                                \tag{26}
$$

其中

$$
B_0=\frac{15\delta-4\alpha-8\beta-12a}{26},\qquad
C_1=\frac{8\alpha-10\beta-28a-43\delta}{26}.                     \tag{27}
$$

它对全部真实开平端路径适用，边界势由共同常值 germs 支付；不是删去累计项后的局部替代成本。下一真实正字符问题是：在 (25) 下，哪些四元组使 (26) 对所有该类路径非负。本次没有运行新标量点、路径表或优化求解。

## 7. 实际完整结果与本轮增量

| 项目 | 全部已成结果 |
|---|---:|
| 已处理字面基列 | 77 / 77 |
| 完整两根转换 | 154 |
| 真实共同矩阵 rank | 52 |
| 新完整函数核关系 | 25 |
| 模旧 B/R168/R174 的新增独立等式 | 7 |
| 复用旧 pure 转换 | 42 |
| 新映射原分量 | 112 |
| 累计原 term steps | 45053 |
| 累计整数消元 steps | 2158 |
| 累计独立原列和 / 转换和 | 各 854 |
| 最大精确系数位数 | 47 |
| cycle fallback | 0 |
| 本次续算时间 | 25.529647644 秒 |
| 本次 peak RSS | 208.59375 MiB |

相对于 R182，本轮追加 15 列、15 条函数关系、28 个新映射分量和两份旧 pure 运输；追加 11631 个原 term steps、671 个整数消元 steps、629 次独立原列及转换相加。已有 primitive 缓存覆盖新增组合，所以本轮新 primitive 调用数为 0；没有省略新列的组合、消元和完整原身份核验。

主报告保留程序的保守标签，本稿通过 §2–§4 的已证定理解释真实 rank/核/头部维数。phase/outcome 优先记录“指定点被切”，但 all_77_columns_processed 明确为 true，不能误读为又停在 62 列。

R177 在八条已付完整关系上取非零值，首条 relation 9 的值 384 与 R182 相同。没有修改该点或重跑旧 86 条必要行。

## 8. 完整公开原件和同源复用

发布目录为 [actions-43676765171-1-character_head_word_relations](../notes/actions-43676765171-1-character_head_word_relations/)。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43676765171-1-character_head_word_relations/character-head-word-relations.json) | 12724 | 68bf26fc88ffea61f5be2e17e11324540f58ff0a4c71f59b87428caef38c1341 |
| [receipt](../notes/actions-43676765171-1-character_head_word_relations/receipt.json) | 43019 | 1e4faea0f993c36021fc769c9e66c313f6e131f8d2d2add418143d14ed724dfa |
| [完整核证书 gzip](../notes/actions-43676765171-1-character_head_word_relations/character-head-word-relations-certificate.json.gz) | 773910 | fec2d558a1241a4e0beaedcd80fd03395f7c87bce028cb65357cb804bf434685 |
| 核证书 raw | 3936105 | 88baa9dd0ff0ed3d992d67846cbcb2553b68b455ed99b24cfca926ca382d7647 |
| [全部已成状态 gzip](../notes/actions-43676765171-1-character_head_word_relations/character-head-word-relations-state.json.gz) | 1031761 | 951fb294301120dfa1d1ccbbf1821af7730714d428571abbee1356409cb96093 |
| 全部状态 raw | 5148309 | 1ee519e49ab462c4db861009636ed81c512e2d0e973e822a7643576dc1a275f8 |

旧状态来自 run 43675575597，主报告、receipt、packed/raw hash 与全部冻结源码逐项绑定。driver 仍为 79108 字节，

**1ec5fab96ec173c3e1583b40a124c5c98b3249cec9a87be39db3b3066e31b300**；

固定颜色模块仍为 21642 字节，

**ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9**。

已过的 atom 两项人工仍是前一 run 的 2830 字节报告，

**df38c8cfb7924107920d2f7f35a8405c417dff3a4dac5caf685cd4add8a5884c**。

本次 workflow 按该 lane 的准确 schema、phase、源码和报告 hash 复用它，没有伪造声称重跑的新人工。此前两个绑定失败和首切前缀全部保留。

本权的完整函数呈示已经闭合。后继从 (26) 的真实全路径正性及其他权的未付条件继续，不再以新增孤立列或不完备 normal form 代替已付清的函数核。

