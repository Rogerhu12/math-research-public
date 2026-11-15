# 原无穷远第一连接的七维上界与全部最大子式的二十一阶公共零点

日期：2026-11-15。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿不运行新的矩阵计算。它从原物理曲线的真实切向族构造模 $u^2$ 的完整临界变形，证明原自然无穷远 Macaulay 矩阵的第一连接像至多七维。因此原全矩阵十四个正 Smith 指数中，至少七个不小于二；所有 $4354$ 阶最大子式在无穷远共同消失至少二十一阶。它不声称第一连接恰有秩七，不声称未付的七个所选有理核已存在，也不替代后续实际来源恢复。

## 1. 同一个自然参数和原完整矩阵

令 $u=1/s$，原归一化物理均值为

$$
y(u)=u^5v(1/u)=(u^5,u^4,u^3,u^2,u,1)^{\mathsf T}.
\tag{1.1}
$$

原十七式为十一条 $N_i$ 与六条 $\Gamma_i$。按照
[原低 Koszul 来源的真实成本齐次化](R150-appendix-infinity-weighted-heads-of-paid-low-koszul-sources.md)
的准确定义，

$$
\widehat F_i(u,m)=u^{w_i}F_i(1/u,m/u^{10}),
\qquad
w_i=20\ (N),\quad w_i=25\ (\Gamma).
\tag{1.2}
$$

因为原 $N$、$\Gamma$ 对均值权一、中心二阶矩权二分别具有权四、五，(1.2) 正是均值 (1.1) 下的原物理方程。它没有换成另一参数族，也没有引入 $u$ 的负幂。当前 primitive 整数方程所使用的非零常数行缩放不影响下文任何零恒等式。

将每条 (1.2) 乘以全部 $m^\nu$、$|\nu|\le3$，以原次数一至五输出为坐标，记完整自然矩阵为

$$
\mathcal A(u):\mathbb Q[[u]]^{6188}
\longrightarrow\mathbb Q[[u]]^{4367},
\qquad
\mathcal A(u)=A_0+uA_1+\cdots.
\tag{1.3}
$$

本文使用“来源为列”的方向；它是旧 $6188\times4367$ 生成矩阵的转置。已付事实是

$$
\operatorname{rank}_{\mathbb Q}A_0=4340,
\qquad
\operatorname{rank}_{\mathbb Q((u))}\mathcal A(u)=4354.
\tag{1.4}
$$

第一个等号来自
[无穷物理均值的完整临界系统](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md)
§§3–4：原 $170\times135$ 小投影的七个整数核给 $4212+128$ 的特征零上界，同一原矩阵的模七下界夹成等号。这里不把模 $31$ 的秩当作特征零上界。第二个等号沿用
[原 163 核与射影权](R150-appendix-original-163-square-core-and-projective-chart-degree.md)
的原函数域完整秩。

第一连接定义为

$$
\beta:\ker A_0\longrightarrow\operatorname{coker}A_0,
\qquad \beta(v)=[A_1v].
\tag{1.5}
$$

若用 $v+uv_1$ 代替常数提升，首项只增加 $A_0v_1$，所以 (1.5) 确实独立于提升选择。

## 2. 真实切向平面有二阶临界消失

原双点配对及对角公式为

$$
v(s)^{\mathsf T}Kv(t)=-(s-t)^2q(s,t),
\qquad
q(s,s)=-s^2(s-2)(s+6).
$$

它们是
[零第三矩完整分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)
§5 中对原 $K$ 的精确恒等式。因此

$$
v(s)^{\mathsf T}Kv(s)=
v(s)^{\mathsf T}Kv'(s)=0,
\qquad
v'(s)^{\mathsf T}Kv'(s)=-2s^2(s-2)(s+6).
$$

对 (1.1) 求导，并使用前两个零配对，得到原局部切向量的准确平方

$$
\boxed{
g(u)=y'(u)^{\mathsf T}Ky'(u)
=u^6v'(1/u)^{\mathsf T}Kv'(1/u)
=-2u^2(1-2u)(1+6u).}
\tag{2.1}
$$

特别 $g(u)$ 可被 $u^2$ 整除。取独立参数 $c,d$，定义完整 Hankel 二阶矩

$$
M(u;c,d)=c\,y(u)y(u)^{\mathsf T}
+d\bigl(y(u)y'(u)^{\mathsf T}
       +y'(u)y(u)^{\mathsf T}\bigr).
\tag{2.2}
$$

$y^2$ 及其导数均为真实 Hankel 二阶矩，故 (2.2) 没有离开原十一维物理源。在 $u=0$，

$$
M(0;c,d)=d(e_5e_4^{\mathsf T}+e_4e_5^{\mathsf T})
+c e_5e_5^{\mathsf T},
$$

即原平面 $m_0=\cdots=m_8=0$、$m_9=d$、$m_{10}=c$。

置 $p=Ky$。原物理曲线给 $y^{\mathsf T}p=y'^{\mathsf T}p=0$，所以

$$
Mp=0,\qquad MKM=d^2g(u)\,yy^{\mathsf T}.
\tag{2.3}
$$

同时 $yM$ 为真实 Hankel 三阶张量：它由 $y^3$ 及其导数组成。原最高方程的唯一性于是给

$$
\mathcal L_y(M)=yM.
\tag{2.4}
$$

沿用原完整中心化的两个真实低式

$$
N=4MKM+6(\mathcal L_y(M))_p,
$$

$$
\Gamma=
2\operatorname{tr}((KM)^2)y
+8MKMp-12\mathcal L_y(M):(KMK).
\tag{2.5}
$$

由 $Mp=y^{\mathsf T}p=0$，有 $(yM)_p=0$。又由 (2.3)，

$$
\operatorname{tr}((KM)^2)=0,\qquad MKMp=0,
$$

而对称张量收缩满足

$$
(yM):(KMK)
=\tfrac13\left[
y\operatorname{tr}(MKMK)+2MKMKy
\right]=0.
$$

因此在整条 (2.2) 上，

$$
\boxed{
N=4d^2g(u)\,yy^{\mathsf T}=O(u^2),
\qquad \Gamma=0.}
\tag{2.6}
$$

这里的 $O(u^2)$ 是 $\mathbb Q[c,d,u]$ 中准确的整除性。全部十一条 $N$ 系数和全部六条 $\Gamma$ 坐标都保留了，不是只核某个标量或某个低阶子系统。

## 3. 二十个纯切向坐标杀掉全部第一连接

取任意真实来源 $v\in\ker A_0$，将它的 6188 个坐标按原方程合并为次数至多三的多项式 $a_i(m)$。令

$$
P(u,m)=\sum_{i=1}^{17}a_i(m)\widehat F_i(u,m).
$$

$A_0v=0$ 的意思是完整多项式恒等式 $P(0,m)=0$，而不仅是在切向平面上为零。故可写

$$
P(u,m)=uP_1(m)+O(u^2),
\tag{3.1}
$$

其中 $P_1$ 的原输出坐标就是 $A_1v$。

另一方面，由 (2.6)，把同一个物理图 (2.2) 代入后，

$$
P(u,M(u;c,d))=O(u^2).
$$

在 (3.1) 中比较一次项，严格得到

$$
\boxed{P_1(0,\ldots,0,d,c)=0.}
\tag{3.2}
$$

也就是说，$A_1v$ 的全部纯切向输出系数为零。这些坐标是 $c,d$ 的次数一至五单项式，共

$$
2+3+4+5+6=20
$$

个。由于 $A_0$ 的所有像本来就杀掉纯切向坐标，(3.2) 也是 $\beta(v)$ 在完整余空间里的准确结论。

再用原无穷远秩证书：至少两个横向因子的 $4212$ 维输出空间全部包含在 $\operatorname{im}A_0$；恰好一个横向因子的 $135$ 维空间被原 $170\times135$ 投影覆盖 $128$ 维。因此

$$
\operatorname{coker}A_0
\simeq
\mathbb Q^{20}_{\rm tangent}
\oplus\mathbb Q^{7}_{\rm one\ transverse}.
$$

结合 (3.2)，得到本稿主结论

$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta\le7.}
\tag{3.3}
$$

若未来七个真实来源的第一连接确有七个独立值，(3.3) 就可把该下界夹成完整第一连接秩七；本文没有预填这个尚待执行的下界。

## 4. 完整 Smith 指数及公共二十一阶零点

在离散赋值环 $\mathbb Q[[u]]$ 上对完整矩阵作 Smith 变换。由 (1.4)，有 $4340$ 个单位不变量及十四个正指数

$$
u^{\alpha_1},\ldots,u^{\alpha_{14}},
\qquad \alpha_j\ge1.
$$

第一连接的秩准确等于这些指数中 $\alpha_j=1$ 的个数。此事实可直接在 Smith 对角矩阵逐项核：单位块不产生核，$u$ 块将其常项源送到非零余类，$u^a$、$a\ge2$ 的一次项为零；两侧可逆形式基变换仅改变核和余空间的基，不改变该秩。

由 (3.3)，至多七个指数等于一，所以至少七个指数不小于二。因此

$$
\boxed{\sum_{j=1}^{14}\alpha_j\ge21.}
\tag{4.1}
$$

完整矩阵的 $4354$ 阶最大子式理想正由这些非零不变量的乘积生成，故

$$
\boxed{
\text{每个 }4354\text{ 阶最大子式都可被 }u^{21}\text{ 整除。}}
\tag{4.2}
$$

这是对所有原来源、所有所选最大子式的公共下界，不需要选定子式的高阶来源仍留在固定选列中。它与另一路“29 个真实 Koszul 曲线使指定子式至少 43 阶”的来源论证相容，但不能把两个下界相加。

本稿没有给 $\alpha_j$ 的上界，没有断言它们均为一或二，也没有通过第一次连接完成全部无穷远长度或原目标的特征零成员性。
