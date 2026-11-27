# 原 full47 Gaussian CM 首对数：同一整 Hodge 基中的实际读取

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：来源与本有限算法已纸面核对；此次新计算尚未执行，不预设任何 CM 值非零。**

## 1. 消费的原输入

固定 $X=X_{\rm ns}^+(47)$，$q=4513$，
$u_4=23[y_{1728}]-C_\infty$、$B_q=q+1-T_q$。
[R1091](../results/R1091-original-Gaussian-CM-logarithm-as-one-algebraic-coefficient.md)
已经在原短族
$$
E_z:\quad Y^2=X^3+343X+z,\qquad \omega=dX/(2Y)
$$
上证明，对实际全纯整微分 $\omega_F=F(z)k(z)\,dz$，
$$
q^{-1}\log_J(B_qu_4)(\omega_F)
=\frac{23}{k(0)}[z^{q-1}]F(z)k(z)I(z)\pmod q,
$$
其中
$$
k(z)=-\frac{3A}{4A^3+27z^2},\quad A=343,\quad
H(z)=[X^{q-1}](X^3+AX+z)^{(q-1)/2},\quad
I(z)=\int_0^z k/H^2\,dz\pmod {z^q}.
$$
积分只到 $z^{q-1}$，只除以 $1,\ldots,q-1$；
没有形式除 $q$，没有把尚未收敛的指数级数当成解析函数。

R1086 的原全47标量纤维已认证 $E_0$ 的 trace96、群阶 $2\cdot47^2$、
完整47挠点及同一个原 Gaussian CM 点。
这里消费该输入，不重跑所有twists、标签图或旧盘筛选。

[R1090 §8](../results/R1090-original-weight-one-integral-Hodge-source.md)
的 run45946046378/job140330877264，
源2ca67b3292da189223f9a46af5ee4b01102a424c，
已认证原95维 logarithmic 格与全23留数的73维整 Hodge 核。
本请求以该回执的95个 descriptor 作为明确来源参数，
仅重建所需原级数并核五个实际 SHA-256；
不搜索候选、不重证旧秩。

## 2. 新的实际 Hecke 坐标桥

导入原 Hodge 消费者不会运行其 main。
调用其已证明但首请求未调用的 hecke_bridge，
以真实 Tate 商公式
$$
c_r(T_nF)=\sigma_n^{-1}c_{nr}(F)+n\sigma_n c_{r/n}(F)
$$
读取 $T_2,T_3,T_5$，最高degree835，构造
$M=M_2+2M_3+4M_5$。
采用行作用
$T_n\omega_i=\sum_j(M_n)_{ij}\omega_j$。
所以原点的 log evaluation 列受同一 $M_n$ 作用。

这是新的原基坐标计算。
R1081 的 mod4513 因子次数 $1^{16},2^6,3^4,11,22$
及16个已认证一次根只用作来源一致性检查；
不搬其平方水平矩阵或 eigenvector。
程序实际验证坐标等式、算子交换及完整特征多项式的 squarefree。
若不一致就报告失败及已经完成的步骤，不继续使用错误桥。

## 3. 原47标记及唯一 étale 提升

在 $E_0/\mathbf F_{4513}$ 中按固定字典序选
非零 $P=2R$，核 $47P=0$。
取固定最小平方根 $i^2=-1$，$Q=iP=(-X(P),iY(P))$。
47在 Gaussian 环中惰性，故两点独立；程序也直接核所有47个标量。

用标准 Miller47商计算原 Weil 配对，
其奇数符号为
$$
e_{47}(P,Q)=-f_{47,P}(Q)/f_{47,Q}(P).
$$
若初始值为 $\zeta$，选择 $d$ 使 $\zeta^d=2$，
再选 $r^2+s^2=d$，换 $P\leftarrow rP+sQ$、$Q=iP$。
这保持同一 CM Cartan 项链，并严格使原配对等于2。
最终再次核配对和两点阶。
这里 $(P,Q)$ 对应 $(1/47,\tau/47)$，
Khuri–Makdisi Remark4.2 的配对是 $\exp(2\pi i/47)$，
故与 R1090 的 q 展开根2同向。

只对 $P$ 做一次原 $\psi_{47}(X,z)=0$ 的 Newton–Hensel 提升，
精度 $z^{4513}$；$\partial_X\psi_{47}(P,0)$ 为单位。
除式采用标准递推，奇数 $n$ 取 $f_n=\psi_n$，
偶数取 $f_n=\psi_n/(2Y)$。
初值
$$
f_3=3X^4+6AX^2+12zX-A^2,\quad
f_4=2(X^6+5AX^4+20zX^3-5A^2X^2-4AzX-8z^2-A^3).
$$
奇数递推中 $(2Y)^4=16(X^3+AX+z)^2$ 放在正确的奇偶项；
同时用 dual pairs 精确微分。
最后核完整 $\psi_{47}=0$、导数单位和曲线方程。
$Y$ 用同一非零初值的平方根 Newton 提升。

实际同构 $E_{-z}\to E_z$ 是 $(X,Y)\mapsto(-X,iY)$，
因此第二个原标记的唯一 étale 提升准确为
$$
Q(z)=(-X_P(-z),iY_P(-z)).
$$
没有把 $i$ 当作 $z\ne0$ 纤维的自同态。

## 4. 同一 weight-one $e$ 的完整2208点来源

短模型上用 R1090/R1091 已付清的加法式
$$
e(P+Q)=e(P)+e(Q)+m_Y(P,Q).
$$
斜率前没有 $1/2$。
先对链
$1,2,4,5,10,11,22,23,46$
同时求原点和累计斜率 $L_{46}$，
由 $46P=-P$ 得 $e(P)=-L_{46}/47$。
Gaussian 运输为 $e_Q(z)=-i e_P(-z)$；
程序再用 $Q$ 的独立同一加法链核这个等式。

随后用群加法得到全部 $rP+sQ$，
$(r,s)\in\mathbf F_{47}^2\setminus\{0\}$，
同时按同一加法式得到全部 $e$。
所需分母均在 $z=0$ 是单位：
除明确 doubling 外没有相等或相反的被加点。
程序核全部2208点的方程、互异常数、负号和 Gaussian 作用。
完整点/级数仅在 runner 内存，逐行流式哈希，不生成数据 artifact。

CM grid 的键是 $(r,s)=(\mathrm{real},\mathrm{imag})$。
R1090 的 descriptor $(a,c,d)$ 则表示 $\rho=d+ci$，
原标签 $(c,d)$ 表示点 $dP+cQ$。
所以 $\rho(r+si)$ 的 grid 键严格为
$(dr-cs,cr+ds)$，共轭项为 $(dr+cs,-cr+ds)$。
这个坐标区别在代码中明确保留。

对这95个原形式逐个读取完整
$$
F_{a,\rho}=\sum_{x\ne0}
 \bigl(2^{aNx}e_xe_{\rho x}+2^{-aNx}e_xe_{\bar\rho x}\bigr).
$$
全部46个范数组各有24个半向量，乘二恢复完整和；
两项的相位分开，纯虚 $\rho=2i$ 保留。
每个实际 $F$ 都核 $F(-z)=-F(z)$；
这是原粗 Gaussian 分支的权二下降条件。

## 5. 原 Hasse 权重、首矩与全部整块

原 Hasse 系数用一个完整 multinomial 和读取：
令 $m=(q-1)/2$，取
$$
H_\ell=\frac{m!}{j!\,k!\,\ell!}A^k,\quad
k=2m-3j,\quad\ell=2j-m,\quad
\lceil m/2\rceil\le j\le\lfloor2m/3\rfloor.
$$
这里全部阶乘小于 $q$；程序核 $H(0)=96$ 和偶性。
计算 $k,H^{-2}$ 与短积分 $I$，核 $I'=k/H^2\bmod z^{q-1}$、
$I(0)=0$、奇性，并形成 $W=23kI/k(0)$。

95个首矩为 $[z^{q-1}]F W$。
它们乘同一原 $73\times95$ residue-kernel，
得到73个实际整全纯微分上的 $\lambda_{u_4}$ 列。
R1090 的精确整全纯 lift 已证明这个模q读数的合法性；
不把 arbitrary integer coefficient lift 当成全纯。

对 $M$ 的每个实际不可约因子 $f$，
构造 CRT 幂等多项式
$$
e_f=(\chi_M/f)\,(\chi_M/f)^{-1}\pmod f\pmod{\chi_M}.
$$
读取 $e_f(M)\lambda_{u_4}$，核全部块之和回到原列、
每块被 $f(M)$ 杀掉。
输出每个块的因子、非零/零、投影hash及首个非零坐标。
对16个一次块另取实际左 eigenform，
以其73维原基中的首个非零坐标为1，
输出精确 $q^{-1}\log(B_qu_4)$ 值及 eigenform hash。
不将角代数的 $G$ 根当成这个 $H_2$ 根。

若某块读数非零，R1089 的
$\log J(\mathbf Q_q)\subset q\operatorname{Lie}J(\mathbf Z_q)$
和 $B_q$ 整可逆性给该原 CM 类在这块深度恰1。
由 R1080 的逐因子代数秩一、R1081 的实际未分歧最大整 Hecke序，
原 Mordell–Weil $\mathbf Z_q$ 格在各 DVR 块自由秩一。
写 $u_4=aG$，则
$q^{-1}\log(B_qu_4)=a\,q^{-1}\log(B_qG)$；
两因子都整，乘积是该 DVR 的单位，故二者各自为单位。
因此这个实际 $u_4$ 生成相应原 MW 块，
且其 log 格恰为 $q\operatorname{Lie}$ 的该块。

这是后继依据实际非零结果才能使用的推论。
若该块为零，只报告 $u_4$ 的首层消失；
不自动宣称整个 MW 块是 Wieferich 或高度非零。
任何首log结果都不替代全局 p-adic height 条件或原八盘排点。

## 6. 执行与保留范围

固定官方 SageMath10.6 amd64 image
sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879。
总数学窗口1800秒、reserve60秒；内部1740秒发出未完回执，
外层1800秒停止。所有数学只在本公开仓库 Actions 中执行。
请求锁定两README、两来源证明、Hodge消费者、本方法和CM消费者的hash、
实际checkout SHA、同一有限模型与95来源参数。
没有外部数值服务、没有本地或V8数学执行。

完整原矩阵、2208点级数、95个长形式均不保存。
只保留脚本、参数、run/job、精确小结论与规范SHA-256；
后继需要时从已经认证的源重建并核hash。
预算或异常中断时，回执只保留实际完成的阶段，
未算出的 CM 块、MW 饱和、高度和有理点分类仍开放。
