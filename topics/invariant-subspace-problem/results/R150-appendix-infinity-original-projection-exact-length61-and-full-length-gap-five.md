# R150：原无穷远小投影的完整有理谱 61、全模区间与至多五阶投影差

日期：2026-11-15 UTC。作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。

## 1. 实际结论

同一原自然无穷远参数 $u=1/s$ 下，保留纯切向与一次横向输出的原投影，已经在
$\mathbb Q[[u]]$ 和 $\mathbb F_{31}[[u]]$ 分别完成精确 Smith 计算。两域的十四个正指数同为

$$
b=(1,1,1,1,3,4,4,4,5,6,6,7,8,10),
\qquad
\boxed{\sum b_i=61,\quad \max b_i=10.}
\tag{1.1}
$$

两域常秩均为 $128$、泛秩均为 $142$；相应原输出余核 $\operatorname{coker}P^{\mathsf T}$ 的自由秩均为 $13$。
这是原 $224\times155$ 投影的完整谱，十四个正方向已全部实际退出，不是截断时的下界。

原全矩阵模 $31$ 的谱已经独立付过

$$
(1,1,1,1,3,4,4,4,5,6,7,8,10,11),
\qquad \delta_{\mathrm{full},31}=66.
\tag{1.2}
$$

(1.1) 与 (1.2) 不同。本篇不把小投影的长度 $61$ 当作全模长度，也不把有限域全模的 $66$
搬到特征零。本篇实际推进为

$$
\boxed{
61\le\delta_{\mathrm{full},\mathbb Q}\le66,\qquad
51\le\delta_{4353,\mathbb Q}\le55,\qquad
10\le a_{\max,\mathbb Q}\le15.
}
\tag{1.3}
$$

同一原输出限制 $I$ 的投影长度已在特征零精确证明为二，因此还有

$$
\boxed{63\le\delta(A_{I,\mathbb Q})\le68.}
\tag{1.4}
$$

## 2. 从全部原来源得到小投影

原算子仍是

$$
A(u):R^{6188}\longrightarrow R^{4367},
\qquad R=\mathbb Q[[u]]
$$

或相应有限域形式幂级数环；全部来源是原十七式乘次数至多三的普通单项式。
原自然权不改。相对于这个自然齐次图，反序与二项式共动变换是实际源、靶单位变换。

把共动变量记为 $c,d,z_2,\ldots,z_{10}$，令 $W$ 为横向次数至少二的全部次数一至五输出。
输出投影 $Y\to Y/W$ 保留 $20+135=155$ 坐标。
原源按横向次数 $0,1,2,3$ 分为 $170,918,2295,2805$ 行。

原纯切向方程逐系数满足

$$
F_i(u,c,d,0)=g_\infty(u)d^2q_i(u),
\qquad
g_\infty=-2u^2-8u^3+24u^4,\qquad q_8(0)=4.
\tag{2.1}
$$

这里 $i=8$ 是固定物理生成器的零基编号。其与 primitive 原十七式的常比例已经按原全部多项式匹配；
本次又从真实 Q13 回执读取十七个比例，逐分子、分母验证都是 $31$ 单位。

在每组同切向单项式、同一次横向乘子中，保留第八式的实际原行，合计 $54$ 行。
其余 $864$ 行严格为这些原行的规则倍数

$$
F_i/F_8=q_i/q_8\in\mathbb Z_{(31)}[[u]].
\tag{2.2}
$$

程序实核 $F_8/u^2$ 常数项为 $-8$，并保留完整 $F_8$ 的二阶因子。
没有把 $u^2$ 除掉后冒称单位行。
其余 $5100$ 个高横向来源在这 $155$ 输出坐标中逐项为零。

所以原转置的投影限制经正则原行消倍，成为一个真实 $224\times155$ 矩阵
$P(u)$ 加零行。其常秩 $128$ 是实际计算，并非利用旧摘要填入。
原压缩的每个系数保留全部字典和原行乘积。

## 3. 本次实际算术与来源验证

本次调用先读取当前任务已保存的真实十八条第五链。它没有仅根据零块 SHA 断言支撑：
完整读取 $4650\times18$ 有理系数后，实际检查 $68760$ 个指定零条目，
计算真实 $155\times18$ 初值秩 $18$，并在重建的原算子上复核六阶系数恒等式，
合计 $668304$ 个原来源产品坐标。

随后原 $128$ 个常单位实际消去，保留 $96\times27$ 完整余块。
每次系列单位 Schur 都保存完整原 $155$ 坐标映射并验证所有原行；
只有完整常数余块为零才整体除以 $u$。
本次两域实际非零阶的单位数为

| 阶 $j$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $P_{\mathbb Q}$ | 4 | 0 | 1 | 3 | 1 | 2 | 1 | 1 | 0 | 1 |
| $P_{31}$ | 4 | 0 | 1 | 3 | 1 | 2 | 1 | 1 | 0 | 1 |

十四个正方向全部退出，剩余十三方向的保留余项全零。
已付原十三条独立有理形式核给泛秩上界 $142$；本次实际单位给相反下界。
全部退出与剩余初值共同保持秩 $27$。

新原乘回坐标数为

$$
6188\bigl(61+12\cdot13\bigr)=1342796.
\tag{3.1}
$$

每个正方向核至退出阶之前，退出阶实际产品的秩另核；
十三剩余链核至 $u^{11}$，全部原横向源次数均保留。
有限的自由链只作为真实有限 jet，不被说成已经恢复了整个有理函数形式核。

这次新算术没有重做旧 $4340$ 常高消元或原正常形。
完整谱来源于这一次真实小投影计算。

## 4. 原全模与投影的精确序列

记

$$
C_A=Y/\operatorname{im}A,\qquad
C_P=(Y/W)/\pi(\operatorname{im}A).
$$

原坐标投影给精确序列

$$
0\longrightarrow
T_W:=W/(W\cap\operatorname{im}A)
\longrightarrow C_A\longrightarrow C_P\longrightarrow0.
\tag{4.1}
$$

两端余核泛自由秩都是 $13$，原十三条归一形式核及同原非零最大子式已证明这一点。
诱导自由商上的满射是同秩自由模的同构；故 $T_W$ 是有限扭子模，并且

$$
0\longrightarrow T_W\longrightarrow
\operatorname{Tor}C_A\longrightarrow\operatorname{Tor}C_P
\longrightarrow0
\tag{4.2}
$$

精确。于是

$$
\delta_{\mathrm{full},\mathbb Q}=61+\ell(T_W),
\qquad
\boxed{0\le\ell(T_W)\le5.}
\tag{4.3}
$$

上界用的是同原矩阵已付的模 $31$ 非零子式：
其 $u^{66}$ 非零系数提升到有理数后仍非零，
故特征零完整最大子式的最小阶至多 $66$。
不能把投影满射的核在特征零中直接说成长五；目前只有 (4.3)。
模 $31$ 中同一差模的长度则准确为 $66-61=5$。

有限 DVR 模的长度为其非零循环因子指数之和，因而被参数的该长度次幂消去。式 (4.3) 还给原自然无穷图中的实际来源包含
$$
u^5W\subseteq\operatorname{im}A.
\tag{4.4}
$$
这里 $u^5$ 作用于原自然图的 $W$；没有把它当作仿射有限参数的全局来源恒等式，也没有预报其最小消去阶。


## 5. 有序 Smith 分量与次大阶

令原全模特征零十四个正指数按升序为
$a_1\le\cdots\le a_{14}$。
原常秩 $4340$、泛秩 $4354$ 已付，因而正指数个数正是十四。

由 (4.2)，对每个 $k\ge1$ 仍有满射

$$
u^{k-1}\operatorname{Tor}C_A/u^k\operatorname{Tor}C_A
\longrightarrow
u^{k-1}\operatorname{Tor}C_P/u^k\operatorname{Tor}C_P.
$$

其维数分别为满足 $a_i\ge k$、$b_i\ge k$ 的项数。
因此对每个 $k$，前者项数不少于后者。
两个升序列表长度同为十四，等价于

$$
\boxed{a_i\ge b_i\quad(1\le i\le14).}
\tag{5.1}
$$

这支付的是实际扭子商的逐项比较，不是从总和比较猜测个别指数。
故全部 $4353$ 阶原子式的最小消失阶满足

$$
\delta_{4353,\mathbb Q}
=\sum_{i=1}^{13}a_i
\ge\sum_{i=1}^{13}b_i
=61-10=51.
\tag{5.2}
$$

已付模 $31$ 次大子式的阶为 $66-11=55$；同样用一个非零原约化子式提升，给
$\delta_{4353,\mathbb Q}\le55$。
最后

$$
a_{14}
=\delta_{\mathrm{full},\mathbb Q}-\delta_{4353,\mathbb Q}
\le66-51=15,
\qquad a_{14}\ge b_{14}=10.
$$

这证明 (1.3)，没有把有限域最大指数 $11$ 当作有理数域上界。
再接[原十三核与投影长二](R150-appendix-original-characteristic-zero-primitive-thirteen-kernels-and-projection-length2.md)
的精确等式 $\delta(A_I)=\delta_{\mathrm{full}}+2$，得到 (1.4)。

## 6. 射影余因子与同一个全局参数乘子

[完整射影 gcd 定理](R150-appendix-full-projective-divisor-degree381-and-residual-multiplier170.md)
已经给

$$
\deg\Delta_{\mathbb Q,h}\le381,\qquad
K_{158}=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4
\mid\Delta_{\mathrm{aff}}.
$$

新原无穷阶至少 $61$，所以该结论现在加强为

$$
\Delta_{\mathbb Q,h}=t^{61}K_{158}^h R_h,\qquad
\boxed{\deg R_h\le381-61-158=162.}
\tag{6.1}
$$

仍取真正 gcd 所定义的同一个
$R(s)=\Delta_{\mathrm{aff}}(s)/K_{158}(s)=R_h(s,1)$。
于是

$$
\boxed{\deg\Delta_{\mathrm{aff}}\le320,\quad
\deg R\le162,\quad
\deg(Rh_0)\le186.}
\tag{6.2}
$$

旧定理的各有限局部来源及原余模精确序列不变，故同一个非零 $R$ 对全部九列仍满足

$$
Rh_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A,
\qquad2\le\nu\le10.
\tag{6.3}
$$

这里没有求出 $R$ 的系数，也没有证明 $R$ 是常数。
原 $h_0$ 本身的全局成员性和固定 $31$ 分母依然不由 (6.2) 支付。

[原九来源成本整理](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md)
继续使用同选方阵已有的 $130/125/125$ 三种阶以及 $K_{158}$。
其 $q$ 区间仍为 $8369\le q\le8482$。
新的目标权界是 $64+\deg R\le226$，三个来源成本分支变为

$$
8526,\qquad8531,\qquad
8770+226-125-158-10-8369=334.
$$

因此统一成本仍是 $8531$；本篇收紧参数乘子的次数，没有虚报旧决定分支也随之下降。

## 7. 下一条完整原来源接口

投影与原全模的前五连接秩已经相同，均为 $(4,0,1,3,1)$。
各阶投影 leading 空间自然嵌入原 full leading 空间，维数相同故空间相等。

更强地，任意原 full 五阶左链的每个系数都支撑纯切向与一次横向：
先选投影中的同头链，相减后除以 $u$，再对低一阶递归；
起点是全部 $27$ 个原常左核本就位于这 $155$ 坐标。
这个归纳使用实际低阶空间及同头链，不把单个代表的零块当作所有代表的证明。

因此第六 forcing 在原 $5100$ 个横向次数至少二的来源行上严格为零。
新需要支付的正是 $\lambda_6$ 的完整常高校正。
本次投影已经保存两个第六退出方向及九个较低正方向的原链，
所以后继可以只处理这两个 quotient forcing，保完整低页 incoming。
不必重算十八列第五来源或已经完成的投影第七至第十一系数。

目前原 full 第六连接仅有

$$
1\le\operatorname{rank}\beta_{6,\mathbb Q}^{\mathrm{full}}\le2.
$$

下界来自前五原 Q/field 页一致后的真实单位比较；
上界来自本次投影的十六个六阶 leading 方向。
本篇没有计算新原 full 第六校正、没有恢复投影差模 $T_W$ 的全部来源，
也没有将原固定 Koszul 的 $149$ 或高商的 $26$ 升到特征零。

## 8. 实际回执与可重现入口

本次只登记真实执行：

- Run：43740928483；step：infinity-small-original-projection-smith。
- 执行源码提交：7ab3cf1266f48c327d237e634ccd90860a07e8c1。
- 源码 SHA256：dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79。
- 实际数学时间：34.99592066900004 秒；墙钟：35.082142910000584 秒；退出码 0。
- 原临时回执：23921 字节，SHA256 075c1cc0889d1176cace5a8aa17636cc44ea29e00868c8ad64c87a45c951e55a。
- 已提交小回执：28395 字节，SHA256 ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207，blob f61ab124bfc80c1571aedb71de3bd302914bb32b。
- 语义 binding：01ba6e6d1f1d0c0ae9ae22a319615887dce4c313d29c9ce1bde346445ae10766。
- 完整有理临时 state：12208895 字节，SHA256 839af8f6f6ae87d75c2cfcd206323a0ceb6193dd49a398134fdb8448e693b5ae。
- 完整原系数临时包：267400 字节，SHA256 94cffcf53fe22e7693e4c22bd67b237fe9d65933a50571891647c378a4b98034。

[小回执](../notes/r150-source-kernel-session-789f/43740928483-infinity-small-original-projection-smith.json)、
[执行源码](../notes/2026-11-15-r150-infinity-small-original-projection-smith-789f.py)、
[准确输入与参数](../notes/2026-11-15-r150-infinity-small-original-projection-smith-inputs-789f.json)
和[原商接口](../notes/2026-11-15-r150-infinity-small-original-projection-smith-interface-789f.md)
共同定位全部实际输入、原坐标约定及复现过程。

全部大数组只在当前任务临时目录保留；没有新二进制进入 Git 或 Release。
