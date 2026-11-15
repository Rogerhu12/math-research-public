# R809 — 原 primitive 连接的三个完整 CM13 分量与十八阶角色运输

日期：2026-11-15。**状态：以下特征零全算子身份、固定整逆、逐谱线运输及实际同 q 的连接分解已证明。原负二矩与中央非消失没有据此增加假设。**

R807 已证明原型五 primitive 三维空间经 $\mathcal P_B\nabla$ 同构到
R801 的型四三维空间。本篇回答其准确的 CM13 问题：
这个同构不是逐根交织，交换缺陷甚至整可逆。
它准确分成三个都整可逆的交织分量。
每条旧 primitive 线经原完整连接，同时进入三条新型四线。

三个分量所读的全有限角色比，依次为真正的
$\chi_{17},\chi_{17}^{5},\chi_{17}^{3}$。
这些是全坏处身份；不是仅比较同一个三次特征多项式。
本篇没有改动原 $q_N^*$、E 深条件或 Y-unit 负二观察。

## 1. 固定来源、基与原完整连接

保持 R798、R801、R806、R807 的全部原规范：
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad b=17,\quad c_B=1-\omega^2 .
$$
记 $D=d/dz$、$\zeta=\sigma'/\sigma$，令
$$
\nabla=D-34\zeta.
\tag{1}
$$
使用实际同总权基
$$
\begin{aligned}
E^{(4)}_j&=b^{5-j}\sigma_b^{34}x_b^{3j}, &&0\le j\le5,\\
E^{(5)}_j&=-b^{4-j}\sigma_b^{34}x_b^{1+3j}y_b, &&0\le j\le4 .
\end{aligned}
\tag{2}
$$
在这些基中，连接矩阵 $\mathsf C$ 不随 b 改变：
$$
\mathsf C_{j,j}=-(6j+2),\qquad
\mathsf C_{j+1,j}=-(6j+5),
\tag{3}
$$
其余项为零。

令 $\mathcal H_4,\mathcal H_5$ 为 R798 的原 canonical halfperiod，
$$
P_4=\frac{I-\omega\mathcal H_4}{c_B},\qquad
P_5=\frac{I-\omega\mathcal H_5}{c_B}.
$$
本文实际的两个三维空间是
$$
\mathcal B_4=\operatorname{im}P_4,\qquad
\mathcal V^{\rm prim}_5=\operatorname{im}(I-P_5).
\tag{4}
$$
前者是 R806 的 $(v_-,j=4,10,16)$；后者是 R761 的
$(v_+,a=1,7,13)$，不能相认。

取 $P_4$ 的第0、1、2列为基矩阵 $B_4$，
取 $I-P_5$ 的第0、1、2列为 $B_5$。
这些都是 R798 公开数学矩阵的指定列，没有重新选择来源。
$B_4$ 的第3、4、5行 minor 为 $-11\cdot13\cdot17/(2\cdot3^{14})$，
$B_5$ 的第2、3、4行 minor 为 $7\cdot11/(2\cdot3^{10})$。
所以在原研究素数上它们还是两个投影像的整基。
令 $\mathcal A_4,\mathcal A_5$ 为两个完整空间的原 CM13 算子，
并定义
$$
\mathcal A_4B_4=B_4R_4,\qquad
\mathcal A_5B_5=B_5R_5,\qquad
P_4\mathsf CB_5=B_4J .
\tag{5}
$$
原完整 trace 已给
$$
R_4^3=R_5^3=-\omega I,\qquad
\det R_4=\det R_5=-\omega.
\tag{6}
$$

本篇的八个实际十三纤维在特征零重新生成 (5)。
结果是
$$
\boxed{
J=
\begin{pmatrix}
58/27&-4/27&-496/297\\
1241/27&-323/27&4012/297\\
-6188/27&-238/27&-10234/297
\end{pmatrix},
\quad
\det J=\frac{72828}{11}
       =\frac{2^2\,3^2\,7\,17^2}{11}.
}
\tag{7}
$$
这与 R807 同一个原连接一致。没有把任何辅助模 p 的秩升成特征零结论。

## 2. 三个精确 CM13 分量

在 $\operatorname{Hom}_K(\mathcal V^{\rm prim}_5,\mathcal B_4)$ 上，
令
$$
\mathcal T(X)=R_4XR_5^{-1}.
$$
由 (6)，$\mathcal T^3=I$。因此有唯一的完整分解
$$
\boxed{
J=J_0+J_1+J_2,\qquad
J_r=\frac13\sum_{k=0}^{2}\omega^{-rk}R_4^kJR_5^{-k},\qquad
R_4J_r=\omega^rJ_rR_5.
}
\tag{8}
$$
(8)定义实际原连接的分量，不是另行选择的三个同构。

按 (5) 的同一列基，全部矩阵为
$$
J_0=
\begin{pmatrix}
17539/2376&-494/297&662/297\\
284597/9504&-4097/594&9197/594\\
-1796033/9504&833/594&-35921/594
\end{pmatrix},
\tag{9}
$$
$$
J_1=
\begin{pmatrix}
-12385/2376&551/297&-88/27\\
21913/9504&-527/1188&-170/27\\
-376261/9504&-44149/1188&782/27
\end{pmatrix},
\tag{10}
$$
$$
J_2=
\begin{pmatrix}
-25/1188&-101/297&-190/297\\
65161/4752&-5491/1188&2567/594\\
-2941/4752&32011/1188&-1751/594
\end{pmatrix}.
\tag{11}
$$
其行列式准确为
$$
\boxed{
\det J_0=\det J_1=\frac{64736}{33}
 =\frac{2^5\,7\,17^2}{3\cdot11},\qquad
\det J_2=-\frac{8092}{33}
 =-\frac{2^2\,7\,17^2}{3\cdot11}.
}
\tag{12}
$$
所以三个分量都是同构，不存在一个可以省掉的零模式。

所有 (7)、(9)–(11) 的分母只含2、3、11，
行列式再只涉及7、17；指定整基的上述 minor 另含原已排的13。
在原研究射线的全部研究素数上，这些分母和行列式均为单位。
故原固定格上的 $J,J_r$ 及其逆都是整算子；
不新增射线、p 依赖分母或深度损失。
这是指定固定基中的结论，不将任意另行归一的特征向量系数冒称为单位。

### 2.1 交换缺陷也是整可逆

令 $B=J_1^{-1}J_2$。
由 (8) 得
$$
R_5B=\omega BR_5,\qquad
\det B=-\frac18 .
$$
取迹可知 $\operatorname{tr}B=\operatorname{tr}B^2=0$，
所以
$$
\operatorname{char}_B(X)=X^3+\frac18,\qquad B^3=-\frac18I .
\tag{13}
$$
另一方面，
$$
R_4J-JR_5
=J_1\bigl((\omega-1)I+(\omega^2-1)B\bigr)R_5.
$$
由 $(\omega-1)^3=3\delta$、
$(\omega^2-1)^3=-3\delta$，精确得到
$$
\boxed{
\det(R_4J-JR_5)
=-\frac{72828}{11}\,\omega\delta\ne0 .
}
\tag{14}
$$
(14)同样是原格上的单位。
因此没有非零 $P\in\mathcal V^{\rm prim}_5$
满足 $\mathcal A_4(P_4\nabla P)=P_4\nabla(\mathcal A_5P)$。
这比仅指出“同特征多项式不足以交织”更具体。

## 3. 每一条旧谱线的全部三个真实像

固定 $\zeta_{18}=e^{\pi i/9}$。
R761 的旧标签 $a\in\{1,7,13\}$ 的 CM13 特征为
$$
\mu_a^{\rm old}=-\omega^2\zeta_{18}^{14a};
$$
R806 的新标签 $j\in\{4,10,16\}$ 的特征为
$$
\mu_j^{\rm new}=-\omega\zeta_{18}^{14j}.
\tag{15}
$$
故
$$
\mu_{a+3+12r}^{\rm new}=\omega^r\mu_a^{\rm old}
\quad(r=0,1,2),
$$
标签按18化简。结合 (8)、(12)，实际非零逐线运输为：

| 原连接分量 | 旧 $a=1$ | 旧 $a=7$ | 旧 $a=13$ |
| --- | --- | --- | --- |
| $J_0$ | 新 $j=4$ | 新 $j=10$ | 新 $j=16$ |
| $J_1$ | 新 $j=16$ | 新 $j=4$ | 新 $j=10$ |
| $J_2$ | 新 $j=10$ | 新 $j=16$ | 新 $j=4$ |

每格都是非零像，因为对应的 $J_r$ 是同构。
固定任意一条旧谱线，三个目标互异；
所以**原完整 $J$ 的像在三条新谱线中的投影全部非零**。
不能把 (7) 以“相同 CM13 根”为由替换成 (9)。

反过来，(14)说明严格逐根交织在任何非零旧向量上都不成立。
这里的 $J_r$ 是原来源空间之间的线性算子；
没有将它们命名为已付的六输入物理缩放或新的 p-core。

## 4. 三种全有限角色比

令 $\eta_a^{\rm old}$ 为 R761 的准确九阶角色，
$\eta_j^{\rm new}$ 为 R806 的准确十八阶角色。
两者的理想值都按原相同公式
$$
\eta((u))
=\left[
 \operatorname{Teich}_{\mu_3}(u\bmod2)^{-1}
 (u\bmod17)^{16(\mathrm{label}-9)}
 \right]^{-1}
\tag{16}
$$
定义，保完整 $\mu_{18}$ 提升。

置
$$
\chi_{17}=\psi_{E_{17}}/\psi_0 .
$$
这是实际六次17角色：二处平凡，
十七处单位指数48，三处不分歧而
$\chi_{17}(\delta)=-1$。
因此对表中每一格，逐所有坏处有
$$
\boxed{
\eta_{a+3+12r}^{\rm new}
 =\chi_{17}^{\,1+4r}\eta_a^{\rm old}.
}
\tag{17}
$$
证明在17单位上只是
$$
16\bigl((a+3+12r-9)-(a-9)\bigr)
=48(1+4r)\pmod{288}.
$$
二处的比为1；三处 uniformizer 的比为 $-1$，
与 $\chi_{17}$ 的这三个奇幂完全相同。
所有指定其他 uniformizer 亦相同。
原类数一和完整单位相容性使这些局部表给出全局身份。
没有根据一个13处特征推断 (17)。

按 $r=0,1,2$，三个角色比分别为
$$
\boxed{\chi_{17},\qquad\chi_{17}^5,\qquad\chi_{17}^3.}
\tag{18}
$$
第三个虽是 quadratic17，比前两个小，
仍不可删掉它的三处 uniformizer 负号。

正整数 $m\equiv4\bmod6$ 时，旧合法权为 $m+1$，
而完整正权 Hecke 角色满足
$$
\eta_{a+3+12r}^{\rm new}\psi_0^{2m+1}
=\chi_{17}^{1+4r}\psi_0^{-2}
       \bigl(\eta_a^{\rm old}\psi_0^{2(m+1)+1}\bigr).
\tag{19}
$$
在本题负权端点，准确的 Katz 输入比较是
$$
\boxed{
\nu_{a+3+12r,-2}^{\rm new}
=\chi_{17}^{1+4r}\frac{\bar\psi_0}{\psi_0}
       \nu_{a,-1}^{\rm old}.
}
\tag{20}
$$
旧端点是 $(0,1)$，新端点是 $(-1,2)$；
(20)不是一个共同 Tate twist。
因此旧九阶点空间的椭圆 logarithm 公式不自动成为新的负二公式。
R806 已给新端点的准确 Katz 平方、反射权四中心及 multiplier $+1$；
本篇保留这些区别。

## 5. 同一个实际 G2 的唯一 primitive 预像

保持 R801 的同一 $q=q_N^*$，并记其完整物理 E 深来源
$$
\Omega^{-2}Y_*(Z^2\,1_{E\in p^N}qB_0)
=\lambda^{2N}\nu_{G_{2,N}},
\qquad G_{2,N}\in\mathcal B_4 .
\tag{21}
$$
设 $g_N$ 为其 $B_4$ 坐标。由 (7) 唯一地定义
$$
P_N=B_5J^{-1}g_N\in\mathcal V^{\rm prim}_5,\qquad
P_4\nabla P_N=G_{2,N}.
\tag{22}
$$
这是原真实来源的固定整右逆，不是改变 $q$ 的重新适配。
$g_N$ 的原 $\lambda,\kappa,\kappa^N$、全部最高三十次权、
C 补项和58行都留在 (22) 中。

R801 的实际非零范围内，$P_N\ne0$。
它定义于 K 的同一实际代数参数域。
两端三次特征多项式均在 K 不可约；
故 $P_N$ 与 $G_{2,N}$ 在各自三个共轭谱线中的投影都非零。
这只是非零来源系数，不给其负矩赋非零。

若按 R761 原规范写
$P_N=\sum_a p_{a,N}F_a^{\rm old}$，
由 (8) 定义固定非零代数数 $c_{r,a}$：
$$
J_r F_a^{\rm old}
 =c_{r,a}D_{a+3+12r}^{\rm new}.
$$
于是同一个实际来源准确分为
$$
\boxed{
G_{2,N}
=\sum_{a\in\{1,7,13\}}\sum_{r=0}^{2}
      p_{a,N}c_{r,a}D_{a+3+12r}^{\rm new}.
}
\tag{23}
$$
每条旧线有三个不同的像，所有项必须保留。
同一新线内三项的和仍按原系数相加，不能独立赋零或任意选择平方根。

原指定负二行因此为
$$
\boxed{
\mathcal I_{2,N}
=\lambda^{2N}\Omega^2
 \sum_{a,r}p_{a,N}c_{r,a}
       I^{\rm new}_{a+3+12r,-2,p}.
}
\tag{24}
$$
R806 的每项 Katz 平方身份逐项适用；
它不把 (24) 改成 Katz 值的线性和。

### 5.1 仍须保半周期连接和原单位域

R807 的完整解析身份是
$$
P_4\nabla P_N
=\frac{17\omega}{c_B}
  \sum_{e^3=-b}\frac{y}{x-e}\,U_eP_N,
\tag{25}
$$
其中 $U_e$ 是原 canonical 二挠算子，绝对相位已经定标。
各项全纯；全和有真实 $(X+b)$ 因子。
(25)仍是原负二观察；没有把它替换为旧 $F_a^{\rm old}$ 的裸负一。

未投影连接必须按 R807 保持真实独立
$\sigma(c)\otimes(P_N/\sigma)(v)$：
$$
\nu_{\nabla P_N}
=\Omega^{-1}(c+v)_*
 \bigl((v-33c)\,\nu_\sigma\otimes\nu_{P_N/\sigma}\bigr).
\tag{26}
$$
$Y=c+v$ 的单位域仍是这个和变量的单位域。
加投影后还须保 (25) 的完整二挠标签与相位。
不能把协变导数冒作仅乘 Y，
也不能把 prime-to-p 半周期冒作单个 $\mathbf Z_p$ 测试变量上的自由平移。

## 6. 完整原中央外部没有消失

(21)–(26)发生在已经保原 E 门之后的第一 Y 来源上。
混合 Y 的原 W-unit、逆 Y、帽和浅支条件不因此穿过连接。
原 R801 的完整同域关系仍为
$$
\mathscr X_{N,r}(w)+\lambda^rG_N(\kappa^r,w)
=\lambda^{2N}\frac{6\delta}{c_B}J_T(w)
\quad(r\ge2\text{ 偶}),
\tag{27}
$$
包括全部质量、Y-unit、W-unit 失败支及高阶负矩。
$J_T'(0)=0$ 仍只使 (27) 两侧实际内部/外部导数相反。

本篇提供的是 (24) 的准确三种算术运输和所有连接项。
它没有给 (24) 的非消失，也没有增加可独立置零的原中央行。

## 7. 全局确定性与公开执行

算子由原完整十三纤维求得，含 sigma 比值的34次和奇型 y 的真实导数比。
型四空间维数6，用六个不同 $x=2,\ldots,7$ 的实际纤维确定；
型五空间维数5，用五个不同 $x=2,\ldots,6$ 的实际纤维确定。
原 $x^{3j}$ 和 $x^{1+3j}$ 矩阵的非零 Vandermonde 给全局唯一性。
额外 $x=7,8,9$ 只按各型范围作已存在的完整纤维核验；
没有将有限小素数的特征结果提升为实际算子。

半周期由全部三个 E[2] 加法式及同一个原 S 锚产生，
连接由 (1)直接微分给 (3)。
因此 (5)、(8)–(12) 是特征零恒等式；
(14)另由 (12)、(13)手算推出，无新增执行要求。

公开回执：

- source commit：35d9b82b4be396ebee6455bf7ab11a285a5d4e29；
- request：rank2-r809-original-primitive-connection-cm13-20261115；
- GitHub Actions run：[43744465644](https://github.com/Rogerhu12/math-research-public/actions/runs/43744465644)；
  job：132904598912；
- 脚本：[check-r806-primitive-connection-cm13-intertwining.py](../scripts/check-r806-primitive-connection-cm13-intertwining.py)；
  文件前缀沿首次提交保留，结果在本篇 R809 登记；
- 参数：--workers=4；python-flint 0.9.0；
- script SHA256：63afaf39ee52d57e4be3f3f1fb2aa07f35132bd3aac164827f04d23726fff7cb；
- stdout：3461 bytes；
  SHA256：552391bed25da65b6405a9da8d866c60a714cdc80082605d2b643d5e189c838b；
- 全部来源方程、三分量合式、三个扭交织式和原 fulltrace 均 PASS；
  不持久化可重算输出。

准确依赖：

- [R798](R798-original-halfperiod-two-types-and-e-depth-second-source.md)：全 canonical halfperiod、两原空间与全 CM13。
- [R801](R801-original-nonzero-second-e-source-and-complete-negative-two-row.md)：同 q 的真实 G2 及全部外部。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：实际十八阶角色、正/负 root、Katz 负二规范。
- [R807](R807-original-projected-connection-and-native-second-source.md)：原完整连接、唯一 primitive 预像、半周期交换子及真实卷积。
- [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)：旧九阶来源及其真实负一/点空间。
