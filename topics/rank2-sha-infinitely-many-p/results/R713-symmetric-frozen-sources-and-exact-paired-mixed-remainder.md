# R713 — 同四十五整逆的双冻结 S、真实配对域与未消混合首行

日期：2026-11-15。**状态：已证明。**

本篇沿 R702 的同一个实际四十五阶整逆，构造两冻结来源都为 S
的新测试，同时保持 cd-S、native-W=T、第二态 S/new 适配和原
二阶规范。原两支的 I/O/X 过滤因而具有完全相同的系数。

两支可以严格换元成**同一个原测试、同一个观察、两个相反的真实域**。
交域确实消去，但剩余的 T/S 相对观察仍是一个完整混合对数。
本文显示其首行就是同一 cd 权的 Z 一阶条件 Y 来源的负一矩，
没有从两个纯 S 过滤式推出这条首行归零。

同一整逆还产生一个实际中性差：全部已有来源和归一词行都零，
原二阶系数却为一。因此原负一深支的非零仍须通过这个混合首行和
完整补域连接，不能只由正规词行的零宣布矛盾。

## 1. 原四十五条测试的整线性返回

保 R702 的全部参数、旧射线相对密度一子族和 $p>163$ 固定坏集。
令
$$
\mathcal M=\mathbb M_{702}(\lambda,\kappa,\kappa^N,\eta)
\in\operatorname{GL}_{45}(\mathcal O),\qquad N\in4\mathbf Z_{>0}.
\tag{1}
$$
它的四十五列均为真实 $\pi_4$ 中性测试；没有新增目标归一列。
这里直接使用已付整逆，不重跑或改选一个辅助子式。

R702 的八条完整兼容关系仅连接 cd-Y、native-W 和第一 $2Y$
第二态，不限制两份冻结来源。因此可指定任意六个整常数
$$
c_0,c_1,s,t,v,j\in\mathcal O
$$
为完整目标
$$
\boxed{
\mathscr U_0=c_0S,\quad \mathscr U_1=c_1S,\quad
\mathscr B=sS,\quad \mathscr W=6\delta tT,\quad
\mathscr Q=\frac{\omega^2s}{2}S(2z)+vS_{\rm new},\quad
\mathfrak j_2=j .
}
\tag{2}
$$
理由是 S、T 在原二/四挠除子上为零，
$P_2S_{\rm new}=0$，而 $S_{\rm new}$ 在 E4 为零；
(2) 满足 R702 的全部兼容关系。

取 (2) 的四十五行，减去 R594 原基准测试的相同行，
再乘 (1) 的完整逆，即得唯一使用那四十五列的实际测试。
系数整，仍保原六支、C 单位、D 深和全 E 次数逆；
最高权三十次、全部高 C 矩与实际 $\lambda,\kappa,u$ 不变。
其完整 $\pi_4$ 返回仍是 $\lambda^N\pi_{4*}\mu_0$。

特别取
$$
\boxed{(c_0,c_1,s,t,v,j)=(1,1,1,1,1,1)}
\tag{3}
$$
并将测试记为 $q_N^{\rm sym}$。
它是新的实际测试，不把 R702 已发表的 $(1,0,1,1,1,1)$ 改名。
二者相差 (1) 给出的纯中性列组合。

(3) 保留 R702 式(42)的整个 E 深三态表：
物理 Y 来源为
$$
\lambda^{2N}
\left(S,\ \frac{\omega^2}{2}S+[1/2]_*S_{\rm new},\
              \frac{\omega^2}{2}S-[1/2]_*S_{\rm new}\right),
\tag{4}
$$
W 来源为 $\lambda^{2N}6\delta(T,T,-T)$。
原 E 浅的整个 $\Xi$、参考、外谱仍准确按该篇式(45)保留。
本篇改变冻结系数，不改变那条浅来源身份。

### 1.1 原浅层 Xi 的精确余量

令 $\Xi$ 为 R465 原第二态的完整第一 $2Y$ 来源，并写
$$
\Xi_+=\Xi-\frac{\omega^2}{2}S(2z),\qquad
d_N=\lambda^N-\lambda^{2N}.
$$
同一个 $q_N^{\rm sym}$ 在 E 浅门的物理 Y 来源严格为
$$
\boxed{
\left(d_NS,\ \frac{\omega^2d_N}{2}S+U_N,\
                  \frac{\omega^2d_N}{2}S-U_N\right),\qquad
U_N=\lambda^N[1/2]_*\Xi_+-\lambda^{2N}[1/2]_*S_{\rm new}.
}
\tag{4a}
$$
这只使用原完整 $\pi_4$ 中性及 (4)，没有把中性式穿过新 unit 门。
因此没有产生一个新的未知 Xi：
原 Href 和全部外谱在 E 深门的第一推前为零，
在 E 浅门准确是原未加权系数乘 $\lambda^N$。

例如原 $c_H=-(1+\delta)/(2016b)$ 的参考整行是
$$
\lambda^Nc_H\langle2\rangle^{-d_pw}J_H(w),\qquad J_H(0)=1+\lambda.
\tag{4b}
$$
新秩二行的系数是
$(52\lambda^N/3-\lambda^{2N})\langle2\rangle^{-d_pw}$；
其余原谱系数仍为 $\lambda^N$ 倍，没有被赋零。

在实际
$\{E_{YW}\notin p^N,\ v_p(Y)=a,\ v_p(Z)=b_0\}$ 上，
用观察 $f_w(Y/p^a)$，(4a) 的反 R 部分准确乘
$$
(-\lambda)^a(-\gamma\lambda)^{b_0}
 (1+\gamma\lambda)\langle\lambda^2\rangle^{a d_pw}.
\tag{4c}
$$
这来自 R692 的完整 Y/Z 矩形和原物理反射。
当 $a>b_0$ 时，W、V 的实际赋值都是 $b_0$；
特别 $b_0=0$ 时它确在原 W/V-unit 的进入支内。

(4b) 的原参考质量不为零，所以不同 a 的归一参考导数差仍是
$$
\lambda^Nc_H(-\gamma\lambda)^{b_0}(1+\gamma\lambda)
 (1+\lambda)\,a d_p\log\langle\lambda^2\rangle .
\tag{4d}
$$
另一方面整个 $\Xi_+$ 的 unit 质量为零。
其参考与外谱的质量在完整和中抵消，故不能把 (4d) 直接赋给
未投影的整个 $U_N$。三原中央零仍只消相应 S/new 行。


## 2. 两支的实际观察和 I/O/X 分区

保原整数旋转
$$
\mathsf J(c,d)=(d,-c),\qquad \mathsf J_*\mu_0=-\mu_0 .
$$
令
$$
Q=c+2d,\quad L=2c-d,\qquad
Y_j=A+Q\circ\mathsf J^{-j}\quad(j\in\mathbf Z/4\mathbf Z),
$$
所以
$$
(Y_0,Y_1,Y_2,Y_3)=(A+Q,A+L,A-Q,A-L).
\tag{5}
$$
相应真实测试和 T 观察是
$$
q_j=q_N^{\rm sym}\circ\mathsf J^{-j},\qquad
W_j=W\circ\mathsf J^{-j}.
\tag{6}
$$
所有 G 和 carry 门均随 (6) 运输。

对 $n\ge N$，记 $s_n=(-\kappa)^n$；
$P_{Y_j,s_n}$ 缩放原 $Y_j$ 而固定其五个正交伙伴。
对 $Z_j=Y_j$ 或 $W_j$ 使用同一个完整观察
$$
f_w(Z_j\circ P_{Y_j,s_n}^{-1}),\qquad
f_w(x)=1_{x\in\mathcal O^\times}\langle x\rangle^{d_pw}.
\tag{7}
$$
逆映射只在原 $Y_j$ 深域上使用。

定义
$$
\begin{aligned}
\mathsf{CD}_N&=\{c,d\in p^N\},&
\Gamma_{jk}(n)&=\{Y_j,Y_k\in p^n\},\\
\mathsf V_{i,n}&=\{Y_i\in p^n\}\cap\mathsf{CD}_N,&
\mathsf I_n&=\Gamma_{01}(n)\cap\mathsf{CD}_N,\\
\mathsf O_{i,n}&=\mathsf V_{i,n}\setminus\mathsf I_n,&
\mathsf X_{i,n}&=\{Y_i\in p^n\}\setminus\mathsf{CD}_N .
\end{aligned}
\tag{8}
$$
用 $\mathcal V,\mathcal I,\mathcal O,\mathcal X$ 表示各域上 (6)、(7)
的整个 Mellin 积分，上标 S/T 分别选择 $Z_i=Y_i/W_i$。
它们的质量也包含在定义中。

cd 端点为 S，故原未过滤纯 S 行严格为
$$
\mathcal V^S_{i,n}=\epsilon_i\lambda^{n+3N}J_S,\qquad
\mathcal X^S_{i,n}
=\epsilon_i\lambda^{n+N}(1-\lambda^{2N})J_S,\quad \epsilon_i=(-1)^i.
\tag{9}
$$
设 $\mathsf T$ 为真实序列移位 $n\mapsto n+1$，并令
$$
P_{30}=\prod_{a=1}^{30}(\mathsf T-\lambda^2\kappa^a),\quad
U_{30}=\prod_{a=1}^{30}(1-\kappa^a),\quad
V_{30}=\prod_{a=1}^{30}(1-\lambda\kappa^a).
$$
R669/R693 的整个来源多项式对固定 p、N 仍次数至多三十。
两冻结系数现在都为一，因此
$$
\boxed{
\begin{aligned}
P_{30}\mathcal I^S_{i,n}
 &=\epsilon_i\lambda^{2n+2N+60}U_{30}J_S,\\
P_{30}\mathcal O^S_{i,n}
 &=\epsilon_i\{\lambda^{n+3N+30}V_{30}
          -\lambda^{2n+2N+60}U_{30}\}J_S,\\
P_{30}\mathcal X^S_{i,n}
 &=\epsilon_i\lambda^{n+N+30}(1-\lambda^{2N})V_{30}J_S .
\end{aligned}}
\tag{10}
$$
这里是整个 Mellin 身份，不只中央导数。
每个移位仍使用自己的实际域及 (7) 的归一观察。
特别
$$
P_{30}(\mathcal I^S_{0,n}+\mathcal I^S_{1,n})
=P_{30}(\mathcal O^S_{0,n}+\mathcal O^S_{1,n})=0
\tag{11}
$$
不需要假设 $J'_S=0$。

## 3. 真正配对后，剩下哪两个域

不能在同一个 $\Gamma_{01}$ 上把 $q_1$ 改成 $q_0$。
正确做法是在第1支作完整换元 $x=\mathsf Jy$。
因为
$$
Y_1\circ\mathsf J=Y_0,\quad
Y_0\circ\mathsf J=Y_3,\quad
q_1\circ\mathsf J=q_0,\quad
W_1\circ\mathsf J=W,
$$
且 $\mathsf J$ 为原整 unitary 变换，
$$
P_{Y_1,s_n}^{-1}\mathsf J
=\mathsf J P_{Y_0,s_n}^{-1}.
$$
因此同一原观察 $Z_0=Y$ 或 W 下准确有
$$
\boxed{
\begin{aligned}
\mathcal I^Z_{0,n}+\mathcal I^Z_{1,n}
=\int &\bigl(
1_{\Gamma_{01}(n)\cap\mathsf{CD}_N}
-1_{\Gamma_{03}(n)\cap\mathsf{CD}_N}\bigr)\\
&\qquad{}\times q_0 f_w(Z_0\circ P_{Y,s_n}^{-1})\,d\mu_0 .
\end{aligned}}
\tag{12}
$$
所有原输入、权、尺度、unit cut 都在同一次换元中运输。
这里的域已经改变，没有把 R678 的同角域权差删除。

两个域的交集准确为
$$
\Gamma_{01}\cap\Gamma_{03}
=\{A,Q,L\in p^n\}.
\tag{13}
$$
由于 $2,5$ 为单位，(13) 蕴含 $\mathsf{CD}_N$。
交域确实在 (12) 中抵消；剩下的是两个严格不同的半边。
在 $Y$ 深域上，它们分别由 $L\equiv-A$ 与 $L\equiv A\bmod p^n$
定义，不是相同的输入事件。

相同换元给整个两支
$$
\mathcal V^Z_{0,n}+\mathcal V^Z_{1,n}=0,\qquad
\mathcal X^Z_{0,n}+\mathcal X^Z_{1,n}=0,
$$
$$
\boxed{\mathcal O^Z_{0,n}+\mathcal O^Z_{1,n}
=-(\mathcal I^Z_{0,n}+\mathcal I^Z_{1,n}).}
\tag{14}
$$
(14) 对 S 和 T 都是原全域恒等式。
它不把 I 和 O 分别赋零。

## 4. CD 域上的 T/S 单位条件确实相同

令
$$
b_Y=(20+3\omega)/17,\qquad Z=W-b_YY,\qquad
X_n=Y/s_n .
$$
R686 的真实整域等价给
$$
\{Y\in p^n,c,d\in p^N\}
=\{Y\in p^n,Z\in p^N,E_{YW}\in p^N\}.
\tag{15}
$$
因此在 (12) 的两个域上 $Z\in p^N$、$X_n\in\mathcal O$，
且
$$
W\circ P_{Y,s_n}^{-1}=b_YX_n+Z .
$$
由于 $N\ge1$，原两个 unit cut 在此处准确相同：
$$
b_YX_n+Z\ {\rm unit}\quad\Longleftrightarrow\quad X_n\ {\rm unit}.
\tag{16}
$$
这项等价只用于 CD 域；不伸到原 $\mathsf X_{i,n}$。

写 (12) 中的带符号域函数为 $\Delta_n^{\rm dom}$，
并置 $B(w)=\langle b_Y\rangle^{d_pw}$。
由 (16)，完整相对行是
$$
\boxed{
\begin{aligned}
&(\mathcal I^T_{0,n}+\mathcal I^T_{1,n})
-B(w)(\mathcal I^S_{0,n}+\mathcal I^S_{1,n})\\
&\quad=B(w)\int \Delta_n^{\rm dom}q_0\,1_{X_n\ {\rm unit}}
 \langle X_n\rangle^{d_pw}
 \left\langle1+\frac{Z}{b_YX_n}\right\rangle^{d_pw}
 \,d\mu_0\\
&\qquad{}-B(w)\int \Delta_n^{\rm dom}q_0\,
            1_{X_n\ {\rm unit}}\langle X_n\rangle^{d_pw}\,d\mu_0 .
\end{aligned}}
\tag{17}
$$
尤其其质量逐点为零；中央导数为
$$
\boxed{
d_p\int \Delta_n^{\rm dom}q_0\,1_{X_n\ {\rm unit}}
       \log\left(1+\frac{Z}{b_YX_n}\right)\,d\mu_0 .
}
\tag{18}
$$
不是先假设各局部质量为零才删一个尺度 log。
由 (11)，过滤后的 T 配对恰等于对 (17) 右侧施同一个 $P_{30}$；
纯 S 部分已经准确消失。
但 (18) 本身尚未归零。

在两个显示域上可统一展开
$$
\log\left(1+\frac{Z}{b_YX_n}\right)
=\sum_{k\ge1}\frac{(-1)^{k+1}}{k b_Y^k}\,Z^kX_n^{-k}.
\tag{19}
$$
原全部 $1/k$ 分母保留。
因为 $Z\in p^N$，第 k 项系数至少有 $kN-v_p(k)$ 层；
首项是原混合负一行，其余尾属于 $p^{2N}\mathcal O$。
每个实际移位继续按它自己的 $X_{n+a}$ 和域使用 (19)，
不能把它们冻结成同一积分。

## 5. 一个真实中性差揭示尚未支付的混合信息

令 $\mathcal R_{702}$ 表示 (1) 定义的实际四十五列右逆。
取其目标：所有两冻结、cd-Y、native-W、第二态 Y 来源为零，
只令 $\mathfrak j_2=1$。
这满足 R702 的全部兼容条件。
在这里不减原基准权，而直接取纯列组合
$$
\boxed{\zeta_N=\mathcal R_{702}(0,0,0,0,0,1).}
\tag{20}
$$
于是
$$
(\pi_4)_*(\zeta_N e_i)=0\quad(i=0,1,2),
$$
$$
Y_*(1_{\mathcal E_N}\zeta_N e_i)
=W_*(1_{\mathcal E_N}\zeta_N e_i)=0,
\qquad \mathcal E_N=\{E_{YW}\in p^N\}.
\tag{21}
$$
减去完整总行后，(21) 在 E 浅门也成立。
全部来源质量和完整 unit Mellin 行均为零，故 R702(44) 的所有
同门归一 Y/W 词行亦**无条件**为零。
没有另给 $\zeta_N$ 猜一个算术身份。

但它的实际四 sigma 二阶系数准确为
$$
J_2(\zeta_N)=
\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N},
\qquad \ell_0=-3\omega/5.
\tag{22}
$$
其余次数仍只可能为 $8,14,20,26$，赋值至少 $-aN$。
同 R702 的原 Q-unit/L-deep 全负矩级数给
$$
\boxed{
v_p(\Delta_{\zeta_N;N,n})
=3n-2N+v_p(I_{\Sigma_5,-1})
\quad(n>N,\ 2n>v_p(I_{\Sigma_5,-1})).
}
\tag{23}
$$
这里 R655 的原负一非零输入未改变，所有高项仍保。

(21)–(23) 说明一个具体有限范围：
仅使用已经支付的完整来源读数、同门归一词行及其线性组合，
不能推出原负一深支为零。
$\zeta_N$ 就是同一真实 carry 家族内的反例方向。
这不排除额外原混合域恒等式；恰好要求下一步支付 (18)、(19)
或它们的同域全补偿，而不能把正规行零再次计作新约束。

## 6. 同一 cd 权的真正 Z 一阶来源

记 $\rho_{cd,N}$ 为 R702(9) 由当前 $q_N^{\rm sym}$ 返回的完整
cd 来源，保其所有伙伴。其第一 Y 来源为 S，未缩放 W 来源为
$6\delta T$。定义
$$
F_{Z,N}(z)=\Omega^{-1}\int Z e^{Yz/\Omega}\,d\rho_{cd,N}.
\tag{24}
$$
Z 与 Y 正交，所以这是原标准 $\mathcal S_{34}$ 的型5整来源，
完整基可取
$$
\boxed{
-\sigma^{34}x^{13-3j}y,\qquad j=0,1,2,3,4 .
}
\tag{25}
$$
其首阶分别为 $5,11,17,23,29$，首系数一。
一般 b 的相应归一系数乘 $b^j$。
(24) 是一个明确的五维完整来源，不能只读取其总质量：
该型本来就是奇型，质量自动为零。

原 cd-T 行在真实小参数 $t=\kappa^N$ 下恰使用
$b_YY+tZ$。对 $t\in p\mathcal O$，其 unit cut 与 Y-unit 相同。
于是保整个 Mellin 权有
$$
\begin{aligned}
&\left.\partial_w\right|_{0}
\left[\int f_w(b_YY+tZ)d\rho_{cd,N}
 -B(w)J_S(w)\right]\\
&\quad=d_p\sum_{k\ge1}
 \frac{(-1)^{k+1}t^k}{k b_Y^k}
 \int_{Y\ {\rm unit}}Z^kY^{-k}\,d\rho_{cd,N}.
\end{aligned}
\tag{26}
$$
特别
$$
\boxed{
(26)=\frac{d_p\Omega t}{b_Y}
 \int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{F_{Z,N}}
 +p^{2N}\mathcal O\qquad(t=\kappa^N).
}
\tag{27}
$$
同一公式适用于真实中性差 $\zeta_N$，但其 (24) 来源尚未被赋零。
下一步必须计算这个五维实际来源与 (22) 的关系，或直接控制
(18) 的同域条件行。
R540 的两条 S6 有限角色和 R655 的 $\Sigma_5$ 身份都不自动
识别 (25) 中任意一条线。

## 7. 执行依据与当前剩余

本篇没有新增数值执行或输出文件。
所用唯一新整逆已在 R702 证明，并有公开
run `43689632357`、job `132737328611` 的同45阶子式，
script SHA256
`1adb03a5a36ffa6c540716a5e3e68de5bba6b61a48b50e2b553ce3b77c240b07`。
(2)、(20) 仅对这个已付实际线性整逆换右端，
不把辅助模数解直接代入实际 p、N。

新增结论是双冻结同系数、(12) 的完整域配对、
(17)–(19) 的同 cut 混合残差，以及 (20) 的真实零正规行方向。
E 浅 $\Xi$ 的参考/外谱、A34 移动 E 门、原 T 外部
和所有相邻角域补偿仍保留；主目标尚未完成。

主要依赖：
[R702](R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)；
[R669](R669-original-double-s-six-dimensional-source-return.md)；
[R671](R671-fixed-depth-cd-return-and-original-exterior-filters.md)；
[R678](R678-original-finite-word-corners-and-negative-one-return.md)；
[R686](R686-original-yz-core-and-same-source-st-unit-failures.md)。
