# R842：原两图短 RR 空间与 D 的295维准确单位解基

**状态：实际准确完成。** 原公开两图消费者已经给出完整
\(T_{11}=H^0(11H-E_2)\)、\(T_5=H^0(5H-E_2)\) 的准确单位解接口，
以及原 \(H^0(3H-D)\) 的295个规范化准确基向量表达式。
这些表达式以原矩阵及已认证单位子式定义；尚未把全部特征零系数展开成大有理数。
原 eta、刚性化主函数和高度仍未完成。

## 1. 实际来源与结果

公开 [run43776927742](https://github.com/Rogerhu12/math-research-public/actions/runs/43776927742)，
compute job133005301364，source ccc94341bcab2c33e4732fcb9d6bce517b6243f3。
数学阶段35.96680945600002秒，101个完整stage；
2026-11-15T23:52:18.590297+00:00正常结束，退出码0、error=null。
core receipt的总秒数35.97019185000002，包含最终收据开销。

原辅助素数为 \(\ell=1000000753\)、original_branch=0、
原 \(\zeta\) 根549966761；从未换原 \(L\)、原 \(b\)、原正规基或原两锚尺度。

| 实际对象 | 大小或秩 | 实际非零子式 mod ell |
|---|---:|---:|
| 原单tau已选列与新sigma列的组合 | 2451独立列 | 483777893 |
| 原435维余商中的新sigma贡献 | 435×81，秩20 | 20×20 Schur子式418985841 |
| 完整T5条件 | 830×1234，秩415 | 628817039 |
| 完整D条件 | 830×690，秩395 | 422341556 |
| D的规范核基 | 690×295 | 自由坐标295×295恒等块 |

T11的415个商行已在全部2451个选定源列上乘回为零，余商补行块为恒等；
T5的415个选定原行已重构完整830行空间；
D核的全部295列已代回全部830个原方程，
并核原自由坐标归一化恒等块。这里没有将部分矩阵的秩当作全局结论。

## 2. 为什么这些有限子式给准确原空间

沿[R838](R838-certified-original-second-derivative-ideal-and-minimal-order3.md)已经准确成立的
\(E_2=\mathcal D_{\rm cusp}+D\)、\(\deg E_2=415\)，
以及原 \(g(Y)=127,\deg H=272\)。
原正规分次基给 \(\dim V_{11}=2866,\dim V_5=1234,\dim V_3=690\)。

### 2.1 两图的T11

两图所有实际齐次源都属于 \(H^0(11H-E_2)\)。
Riemann–Roch给这个原空间维数2451。
新实际2451子式为单位，故所选原列在特征零独立；
包含关系与同维数迫它们恰生成完整T11。

设 \(T_I\) 为2451个实际选定原行组成的方阵，\(R\) 为其415个补行。
准确商算子为
\[
\Pi_{11}(x)=x_R-T_R T_I^{-1}x_I.
\tag{842.1}
\]
这是原矩阵的有限有理式，不是把模ell矩阵直接宣布为特征零矩阵。
子式保证逆存在，并保证式(842.1)在原辅助素点可准确约化；
\(\ker\Pi_{11}=T_{11}\)。

前一run的单tau矩阵只有模ell秩2431。这个事实仍保留，
不把差20解释成已经证明的特征零无穷远额外长度。
本次确实加入原sigma齐次源，使用的是更正后的完整两图证明。

### 2.2 以两张图准确降至T5

对 \(F\in V_5\)，同时要求
\[
\Pi_{11}(\tau^6F)=0,\qquad \Pi_{11}(\sigma^6F)=0.
\tag{842.2}
\]
因原 \(\tau,\sigma\) 没有共同零点，式(842.2)当且仅当
\(F\in H^0(5H-E_2)\)，不是只在一张图判断。
该核维数819，故原条件矩阵准确秩415。
实际415子式628817039再次认证所选行的完整性；
其415行商保留全部830个原条件，而没有删掉无穷远条件。

### 2.3 原D的完整短核

R837的两个原锚 \(u,v\in V_2\) 的共同零恰为
\(\mathcal B=\mathcal D_{\rm cusp}+P_0\)。
对原 \(F\in V_3\)，使用两个条件
\[
\Pi_5(uF)=0,\qquad\Pi_5(vF)=0.
\tag{842.3}
\]
R836的完整整商恒等式
\(I_D=(I_2:I_{\mathcal B})\)，连同R838的 \(P_0\notin D\)，
给式(842.3)的核准确为
\[
W_D=H^0(3H-D),\qquad \dim_L W_D=295.
\tag{842.4}
\]
因此其原830×690矩阵K准确秩395。
这里使用完整整商，未以形式分式商忽略P0截断。

记实际395个选定行、列为 \(I,P\)，其余295列为 \(F_{\rm free}\)。
每个 \(f\in F_{\rm free}\) 的准确基向量定义为
\[
w_f=e_f-\sum_{j=1}^{395}
       \bigl(K_{I,P}^{-1}K_{I,f}\bigr)_j e_{P_j}.
\tag{842.5}
\]
原子式模ell为422341556，故它在原数域不为零。
准确原矩阵的秩已经是395，因而这些向量满足全部原方程；
自由坐标恒等块证明它们独立。它们就是原W_D完整基，
不是某个有限域核对特征零的猜测。
实际690×295约化矩阵、完整乘回及所有I/P/free索引均已在artifact保存。

## 3. 本次只完成真正缺少的算术

原单tau的2866×2886矩阵、2431个独立列选择、旧sigma系数0..3、
原S5同素点选行逆及已成Fourier前缀均直接复用。

新sigma层只消费原无穷远单位minor所指定的20列，
续求系数4..9并验证最高层结构零与原次数界；
原保存的sigma方向g已经带负号，执行中没有再加第二个负号。
它们按原权与反转关系给81个新齐次移位列。
只在旧435维余商中计算435×81的增量秩20，
再将20阶Schur块与旧选行子式合成真实2451子式。
组合行序明确是旧选行后接选定旧补行；
列序是旧tau列后接所选sigma列，未忽略置换符号。

其后两个原锚与690个V3的全部新乘积在原1380坐标中形成，
以已有同素数S5逆求解并逐个全坐标乘回。
实际使用原 \(82^4,82^6,82^{10}\) 的尺度；
没有为得到好看的模矩阵重新缩放原截面。
两个锚各41个产品组被原子保存，可供后继复用。

整个消费者使用2919个原成员：
R827为529、R809为1242、R786为1115、R837为11、R838为8、
旧单tau R839为14。来源扩展指纹
016087b3ecaede48df3a719d33026b9165bc71e3f256e417d3d9dea7a617ae9f。
这是旧2782源、123件sigma补源和14件已结束R839输出的实际并集，
不是重新生成旧输入。

## 4. 可复现代码、证明和真实产物定位

| 项目 | bytes | SHA256 |
|---|---:|---|
| core R839_two_chart_short_RR_spaces.py | 38335 | 6fe0a0d3f37592b1ac3081a8347a205503de41cdd54e41a05529c837a7b3c73e |
| wrapper R839_two_chart_public.py | 34726 | f27a4585deb43880e162b337a9c6b39528086ce864ea12e17c23192cbb260d2a |
| source request | 3308 | b176f52a6b65dc7f869583265c1eebd3f9947cd4451845e72cc161e11e958772 |
| full manifest，111条 | 18828 | 5bb824d2697e369af3a65ff76cdbe2029ce92d153723c4f5012288118d36e1ba |
| final certificate | 507973 | 51dff9f0b9fff3117b93a4281c21c0cf37a487c0b09bc88a18f8ffdb80d878fe |
| stage manifest，101阶段 | 166837 | d3246312c9a3e65d99d84f864da5357846ea9f002cd7835c6d0e26b7250bc693 |
| T11 unit quotient | 5338200 | 924a944e45142f99ae63aaa0a8a936127a96e323d4a9f9a702bb0b0647d4cbf9 |
| T5 independent row quotient | 2416697 | 8b13bfeef9658e1472a8a06702ea7a247e4070f43c8e13e3251d2a551ff765a9 |
| original D short kernel matrix | 3059616 | 42e09dcc9ccac6cfc35bc4338679c26de7d4bfe1ff3bdd1454850768f6cc2003 |
| original D unit kernel basis | 756940 | ec71c061e59d34bd9e2eb6b38d071b8b53c169443e538956d34e50c6f0e3af60 |
| original S5 fixed-place matrix | 8341255 | 1c1647ea17b1c8cc77e38ba589d1426efee6c165312b090c6823663d6cde1219 |
| 2919原件最小输入carrier | 115520589 | a1f8b947e14f80634a345608e9e5a77feb513facbcee11240297fb44b1e74aa5 |
| 原输入inventory | 502018 | 4dea28a76c2e3a6058594ded3fa4676c9170ccef4fd9ec399a41f59ed6001b3d |

完整配置指纹7597a9d59b4f8fb08548891a298d76cbc745a72245b6e9cb35f973a25ee4fcc4。
其证明依赖为：
更正R839证明f0044713eaa2332531ae7354566e4c72de25d50786efa644fb2524eb6a4c6629；
两图补全证明e9269c0e9352bbc9933f0bdb4a7837615547266d00226dfc234b00e6e24436eb；
执行方法c649f95f49abc94c6cd672e61d51d49c4f1394c90cb8b8449c166af01d4f4649。

实际artifact14186901203，名称
serre-global-R839-original-two-chart-short-RR-spaces-and-D-kernel-43776927742-1，
192975030 bytes、113成员；
平台ZIP SHA256为9a4b0b02988784492bd958859096ee7307e1091ae8c5661eedd91e2fcfe77f50，
到期2026-11-16T23:52:18Z。
reference为236 bytes、dcf721174617f2cb6d811e162a377c6b0cc0bf48e79de9b91bd93d40acc08069；
core receipt为726 bytes、c9ed32d199f9bc744f7248c8840beef91cd99bf29c1e441442b32bfb223278a9，
run receipt为461 bytes、88ac7c4f2b5887280dafac4181274a9c45a0188cafd853ed385c0476048d88ef。

本地只有IO：先14Range/3735758 bytes取21小件，
再4Range/12167945 bytes取D矩阵、D基与S5矩阵，
再4Range/7764937 bytes取两个商。
所取26件（包括manifest/reference）逐一size/SHA正确，
组合指纹b90ab343033ec7cdfff53b79f655b93f5159cad7d1c579957b17ade83ca3e3eb。
没有本地重算秩、乘积或核；没有本地重hash整个193MB ZIP或115MB carrier。
原公开wrapper已经核全部输出及2919原输入字节；本地不夸大自己的读取范围。

## 5. 直接后继与保留边界

现在后继可以按式(842.5)消费真正的完整W_D，
包括给D选两个准确截面、构造原完整极理想或进行所需理想运算。
原两图、单位解、free坐标和尺度必须随来源一起运输；
不得把模ell的690×295数组独立当作一个新特征零基。

本结果不恢复完整Mg/Γ，也不取代R787/R824的准确展开关系。
原单tau源不足的记录仍有效；不再重跑同一2431矩阵、
已完成导数、旧CM迹或同素数S5逆。
原五个加法映射极除子、eta类、主函数的常数/刚性化、
原第二类周期及高度仍须继续。

## 来源

- [R836短核证明](R836-original-reduced-D-fixed-branch-pencil-and-short-RR-kernels.md)、
  [R837原固定两锚](R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md)、
  [R838完整I2](R838-certified-original-second-derivative-ideal-and-minimal-order3.md)。
- [R839原短RR更正证明](../notes/R839-original-short-RR-and-D-kernel.md)与
  [已结束单图及两图补全](../notes/R839-ended-tau-source-rank-and-two-chart-completion.md)。
- [本次两图执行方法](../notes/R839-original-two-chart-short-RR-and-D-kernel-method.md)及
  [原请求](../notes/R839-two-chart-public-request.json)。
