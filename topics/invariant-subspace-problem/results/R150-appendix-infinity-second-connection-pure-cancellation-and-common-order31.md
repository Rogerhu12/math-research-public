# 原无穷远第二连接的纯切向消去与公共三十一阶

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿证明原自然无穷远的完整第二连接秩至多三。原十四个正 Smith 指数中，准确四个等于一、至多三个等于二、至少七个不小于三。因此全部原 $4354$ 阶最大子式在无穷远共同消失至少 $31$ 阶，全部 $4353$ 阶子式至少 $28$ 阶。特别，剩余十个正指数不可能都等于二。

证明只增加一个 $38\times10$ 的真实二阶纯切向计算；没有重算旧正常形，也没有假设小切向来源关系都能扩成完整来源。实际计算给出该矩阵完整为零，并验证全部原 $170$ 行的十列二阶左校正。本文不声称完整第二连接恰有秩三，不声称共同消失阶恰为 $31$。

## 1. 原自然图与已付的完整第一页

取原自然参数 $u=1/s$，均值为

$$
y(u)=(u^5,u^4,u^3,u^2,u,1)^{\mathsf T}.
$$

原成本齐次化的全部十七式与全部次数至多三的来源构成

$$
A(u):\mathbb Q[[u]]^{6188}\longrightarrow\mathbb Q[[u]]^{4367},
\qquad
A=A_0+uA_1+u^2A_2+\cdots.
\tag{1.1}
$$

参数系数不含阶乘，即 $A_2$ 是 $u^2$ 的系数。

沿用
[原双图四维第一连接证明](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)：
原完整常数秩为 $4340$，函数域秩为 $4354$，并且

$$
\operatorname{rank}_{\mathbb Q}\beta_1=4,
\qquad
\beta_1(v)=[A_1v]\quad(v\in\ker A_0).
\tag{1.2}
$$

完整常数余空间分成二十维纯切向部分与七维一次横向部分。第一页的像完全位于一次横向部分，故第二页目标维数为

$$
\dim E_2^T=\dim\operatorname{coker}A_0-\operatorname{rank}\beta_1
=27-4=23.
\tag{1.3}
$$

二十个纯切向泛函与已付的三个一次横向泛函，给这个目标的完整对偶基。这里没有遗漏原六个均值梯度，也没有转用较小的来源包。

## 2. 原二阶纯切向项

如前稿，先作真实物理反序，再作可逆共动矩变换

$$
m_j(u)=\sum_{k=0}^j\binom jk u^{j-k}n_k,
\qquad c=n_0,\quad d=n_1,\quad z_j=n_j\ (2\le j\le10).
\tag{2.1}
$$

在此节的反序坐标中，原均值为 $v(u)=(1,u,\ldots,u^5)^{\mathsf T}$，原矩阵为
$K^\sharp_{ij}=K_{5-i,5-j}$。记反序后的矩阵变量和物理残量为 $M^\sharp,N^\sharp$；它们是原变量的同一常数反序运输。原 $K$ 及其完整十七式的定义均保持前稿。

令横向坐标全零，则

$$
M^\sharp(u;c,d)=c\,v(u)v(u)^{\mathsf T}
+d\bigl(v(u)v'(u)^{\mathsf T}+v'(u)v(u)^{\mathsf T}\bigr).
$$

原真实恒等式给

$$
\Gamma=0,\qquad
N^\sharp=4d^2g(u)v(u)v(u)^{\mathsf T},
\qquad
g(u)=-2u^2(1-2u)(1+6u).
\tag{2.2}
$$

所以全部原式的常数与一次项在切向平面上严格为零。二阶项也可直接写出。反序后的

$$
p_0=K^\sharp e_0=(0,0,0,0,-1,-1)^{\mathsf T},
\qquad
p_0^{\mathsf T}v(\zeta)=-\zeta^4-\zeta^5.
$$

$u^2$ 项来自 $g_2=-2$，故

$$
[u^2]\bigl(v(\zeta)^{\mathsf T}K^\sharp N^\sharp K^\sharp v(\zeta)\bigr)
=-8d^2(\zeta^8+2\zeta^9+\zeta^{10}).
\tag{2.3}
$$

按 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 的固定顺序，完整二阶纯切向系数列准确为

$$
F_2(c,d,0)
=d^2(0,0,0,0,0,0,0,0,-8,-16,-8,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.4}
$$

这是原物理公式的系数，不是从有限域小像猜出的模式。

纯切向目标空间是 $c,d$ 的总次数一至五部分，共二十维。(2.4) 及来源次数至多三表明，原二阶纯切向项只可能落入十维空间

$$
\mathcal P=d^2\mathbb Q[c,d]_{\le3}.
\tag{2.5}
$$

其固定单项式次序为

$$
d^2,\ d^3,\ cd^2,\ d^4,\ cd^3,\ c^2d^2,\
d^5,\ cd^4,\ c^2d^3,\ c^3d^2.
\tag{2.6}
$$

这一步仅给包含关系，尚未给完整第二连接的下界。

## 3. 全部切向一阶关系的二阶纯包络实际为零

保留前稿的原矩阵

$$
P_0,P_1\in\mathbb Q^{170\times135},\qquad
\operatorname{rank}P_0=128.
$$

其行是原十七式乘全部 $c^ad^b$、$a+b\le3$，列是全部 $c^ad^bz_j$、$a+b\le4$、$2\le j\le10$。取完整核基

$$
P_0Q=0,\quad Q\in\mathbb Q^{135\times7},
\qquad
P_0^{\mathsf T}U=0,\quad U\in\mathbb Q^{170\times42}.
$$

已付的四维第一连接包络为

$$
C_{\rm tr}=U^{\mathsf T}P_1Q,\qquad
\operatorname{rank}C_{\rm tr}=4.
$$

再取

$$
Z:\mathbb Q^{38}\longrightarrow\mathbb Q^{42},
\qquad
\operatorname{Ran}Z=\ker C_{\rm tr}^{\mathsf T}.
\tag{3.1}
$$

令 $S\in\mathbb Q^{170\times10}$ 把 (2.4) 乘以各行的纯来源单项式，并读出 (2.6) 的系数。即行 $(i,a,b)$ 只在列 $c^ad^{b+2}$ 上非零，系数是 (2.4) 第 $i$ 项的 $d^2$ 系数。

任意真实第一页来源 $v_0$ 的纯切向来源系数 $a\in\mathbb Q^{170}$ 满足

$$
a=U\xi,\qquad C_{\rm tr}^{\mathsf T}\xi=0,
\qquad a=UZ\eta.
\tag{3.2}
$$

第一式来自完整 $A_0v_0=0$，第二式来自完整 $\beta_1(v_0)=0$。本稿只用这个必要条件，没有假设每个 $UZ\eta$ 都来自真实来源。

新计算直接给出

$$
\boxed{Z^{\mathsf T}U^{\mathsf T}S=0_{38\times10}.}
\tag{3.3}
$$

独立的秩检验为

$$
\operatorname{rank}[\,C_{\rm tr},U^{\mathsf T}S\,]
=\operatorname{rank}C_{\rm tr}=4.
\tag{3.4}
$$

因此 $U^{\mathsf T}S$ 的每一列都属于 $\operatorname{im}C_{\rm tr}$。再用
$\ker U^{\mathsf T}=\operatorname{im}P_0$，存在有理矩阵

$$
W\in\mathbb Q^{135\times10},\qquad
B\in\mathbb Q^{7\times10}
$$

满足原完整行恒等式

$$
\boxed{S=P_0W+P_1QB.}
\tag{3.5}
$$

算法从 $[P_0,P_1Q]$ 的真实可逆 $132\times132$ 子块求出这些列后，验证 (3.5) 的全部 $170\times10=1700$ 个有理等式。它不只核用于求解的子块。

## 4. 十个真实左二阶 jet 与全部原来源

对 (2.6) 中第 $\ell$ 个纯切向目标，令 $\lambda_\ell$ 是取其系数的目标泛函。把 $W_\ell,QB_\ell$ 延拓为仅支持一次横向目标的泛函，定义

$$
\lambda_\ell(u)
=\lambda_\ell-uQB_\ell-u^2W_\ell.
\tag{4.1}
$$

则在原共动矩阵上有完整身份

$$
\boxed{A(u)^{\mathsf T}\lambda_\ell(u)=O(u^3).}
\tag{4.2}
$$

证明分两类来源。

对于纯切向来源，零阶与一阶纯项由 (2.2) 消失；同时 $P_0Q=0$。二阶系数正是

$$
S_\ell-P_1QB_\ell-P_0W_\ell=0.
$$

对于含横向变量的任何来源，$F_0,F_1$ 至少含一个横向变量，所以它们乘该来源后至少含两个横向变量，均被 $QB_\ell,W_\ell$ 杀掉；$F_2$ 乘该来源后不可能产生纯切向目标，也被 $\lambda_\ell$ 杀掉。这覆盖全部 $6188$ 个原来源，包含所有次数至多三的横向来源。

另十个纯切向泛函对应 $d$ 的次数零或一，即

$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d.
$$

它们由 (2.2)–(2.4) 直接以常数泛函满足 (4.2)，不需要二阶校正。因此完整二十维纯切向泛函空间都具有真实左二阶 jet。

若原目标和来源基的变换写成
$A_{\rm new}(u)=T(u)A_{\rm old}(u)V(u)$，则原坐标中的左列是
$T(u)^{\mathsf T}\lambda_\ell(u)$。必须把这个转置运输保留到二阶；不能把共动系数数组直接当作未运输的原左列。

## 5. 与真实来源提升配对，得到完整第二连接上界

第二连接的来源是实际满足 $\beta_1(v_0)=0$ 的 $v_0\in\ker A_0$。选择真实 $v_1$ 使

$$
A_0v_0=0,\qquad A_1v_0+A_0v_1=0.
\tag{5.1}
$$

完整第二连接为

$$
\beta_2(v_0)=[A_2v_0+A_1v_1]
\quad\text{于}\quad
\operatorname{coker}A_0/\operatorname{im}\beta_1.
\tag{5.2}
$$

两种 $v_1$ 的差属于 $\ker A_0$，所以 (5.2) 只改变一个 $\beta_1$ 像，定义良好。

对任一真实左二阶 jet
$\lambda(u)=\lambda_0+u\lambda_1+u^2\lambda_2$，(4.2) 给

$$
A_0^{\mathsf T}\lambda_0=0,\quad
A_1^{\mathsf T}\lambda_0+A_0^{\mathsf T}\lambda_1=0,
$$

$$
A_2^{\mathsf T}\lambda_0+
A_1^{\mathsf T}\lambda_1+
A_0^{\mathsf T}\lambda_2=0.
$$

因此与同一真实提升对 (5.1) 配对后，

$$
\begin{aligned}
\lambda_0^{\mathsf T}(A_2v_0+A_1v_1)
&=-\lambda_1^{\mathsf T}(A_1v_0+A_0v_1)
  -\lambda_2^{\mathsf T}A_0v_0\\
&=0.
\end{aligned}
\tag{5.3}
$$

这正是原来源一阶修正必须保留的位置。它同时解释了为什么在共动目标的常数识别下，完整第二连接的纯切向部分确实为零；这里说的是 (5.2) 的真实提升对，不是把未运输的原 $A_2v_0$ 裸数组当成连接。

第 4 节的二十个 $\lambda_0$ 独立，并属于第二页目标的对偶空间。由 (1.3)，完整第二页目标只有 $23$ 维，所以

$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_2\le23-20=3.}
\tag{5.4}
$$

未消的三个方向正是第一页保留下来的真实一次横向余方向；本稿不声称其像已经全部出现，也不把非纯像自动等同于某个预定空间。

## 6. 完整 Smith 指数和所有子式的共同下界

对 (1.1) 在 $\mathbb Q[[u]]$ 上作完整 Smith 分解。其 $4354$ 个非零指数中，$4340$ 个为零，十四个为正。第一页秩四准确说明四个正指数等于一，其余十个至少为二。

第二连接的秩准确等于正指数恰为二的个数。这可在 Smith 对角形式逐块看出：第一次消去单位块并除 $u$ 后，$u^2$ 块留下一个一次非零连接，$u^a$、$a\ge3$ 的该项仍为零；完整可逆形式基变换只改变各页的基。

由 (5.4)，至多三个指数等于二，故至少七个指数不小于三。于是最大子式除子阶满足

$$
\boxed{
\delta_{4354}\ge4+3\cdot2+7\cdot3=31.}
\tag{6.1}
$$

同理，最小的 $4353$ 个非零指数之和至少为

$$
\boxed{
\delta_{4353}\ge4+3\cdot2+6\cdot3=28.}
\tag{6.2}
$$

所以每个原 $4354$ 阶最大子式都可被 $u^{31}$ 整除，每个 $4353$ 阶子式都可被 $u^{28}$ 整除。零子式当然也满足这些整除性。

这已排除“剩余十个正指数恰全为二”。本稿没有得到 (6.1) 或 (6.2) 的上界，也没有给出某个 $u^{31}$ 首项为 $31$ 单位的原子式。与已付有限 $K_{70}$ 结合后，自然齐次最大子式拥有次数至少 $70+31=101$ 的明确公共下因子；不能把这个公共无穷远下界再机械加到某个已另证的指定子式阶数上。

## 7. 实际小计算与可重建证据

[新增小脚本](../notes/2026-11-15-r150-infinity-second-pure-envelope-789f.py)
复用[已经实际执行的原横向生成器](../notes/2026-11-15-r150-original-transverse-first-connection-789f.py)。它先逐个核对前次已付的 $P_0,P_1,Q,U,C_{\rm tr}$ SHA256，再只构造 $S$、$Z$ 及 (3.3)–(3.5)。

实际运行 43679903558，步骤 infinity-second-pure-envelope，执行源码提交 a1727cdf50bde04ac25248dd15cb8fecf64fb0e9。参数为：

~~~text
--generator <原横向生成器>
--first-connection-receipt <已付完整小回执>
--remaining-seconds 10
~~~

地址空间上限为 $512$ MiB，实际数学用时 $0.251053230$ 秒，退出码 $0$。实际结果：

| 项目 | 结果 |
|---|---:|
| 原第一页包络秩 | 4 |
| 新 $38\times10$ 二阶纯包络秩 | 0 |
| $42\times17$ 增广矩阵秩 | 4 |
| 完整原二阶左校正 | 全部 $1700$ 项成立 |
| 旧正常形重算 | 无 |
| 原大 Macaulay 矩阵重建 | 无 |

脚本 SHA256 为 20ef0ba51ab8c0d25200bf39110db6d6b7c2e53c3c2b368e251fbe46d92a424d。原临时小回执为 $6892$ 字节，SHA256 为 6b3910a8cce4ba39f09b5b1e4a4d5c9e7a112f6db24ae6411a3fb9e705012d6b。

主要真实矩阵哈希：

| 矩阵 | SHA256 |
|---|---|
| $S$ | 4d4dd82bd1612c867137a084821fafc633e29100a57cb1fa27ab3c7f6159a06b |
| $Z^{\mathsf T}U^{\mathsf T}S$ | 39b9c7b36d61ee382a7f087f5646bc7c3628fc248ad3b1adb734b45b3da4a07e |
| 全原 $[W;B]$ 校正 | 1007f5fa9589163f24a14a791254c9b2beb1e8e09e5f476a11e08cf897c1bf12 |

[主线小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-infinity-second-pure-envelope.json)
保存原 seed、十个纯单项式、完整小秩与原校正标志。可重算矩阵仅作当前 job 临时生成，没有上传大数据，也没有以额外审查作为数学运行或发布门槛。
