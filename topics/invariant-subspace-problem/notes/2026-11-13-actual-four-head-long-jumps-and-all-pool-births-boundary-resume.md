# 两个真实四头长跳跃在任意等权池出生层上的三 Gram 观测

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI-assisted，GPT-6 Astra Pro。
状态：以下有限模型的完整源层估计已证明。它不处理原连续非等权尾或全部 $d=2^m$ 实际头。

本稿明确扣除
[R271 回文四头稿](../results/R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md)
§§9–10 已证明的固定 $q=1$、三个位权 $1$ 加八个位权 $\beta$ 的十一位结论。
这里改用两个任意正异常权加任意等权池，允许任意 $q$，
并同时保留原 $N/Y$ 四头的长跳跃。
关键首层 Gram 来自池串的相对真空，不使用原高孔层的统一删除逆。

## 1. 两个实际四头与有限尾

取 $0<\eta\le1/8$。记
$$
A e_1=e_0,\qquad
A e_2=\beta e_0+\eta e_1,\qquad
A e_3=\gamma e_0+\beta e_1+e_2,\qquad A e_0=0.
\tag{1.1}
$$
两种真实四头分别是
$$
(\beta,\gamma)=
\left(\frac14,0\right)\quad(N\text{ 型}),\qquad
(\beta,\gamma)=
\left(\frac14-\eta,\eta\right)\quad(Y\text{ 型}).
\tag{1.2}
$$
后一式由 $N_0-N_0^2+N_0^3+\frac14N_1$ 准确得到，
其中 $N_0^2=\eta N_1$、$N_1^2=0$。
原实际 $\eta_0$ 在上述范围内。尤其
$$
|\beta|\ge\frac18,\qquad |\gamma|\le\frac18.
\tag{1.3}
$$
这里保留 $\beta$ 的非零长跳跃，不能把 $A$ 换成纯单移位。

尾算子取
$$
D=aE_1+bE_2+\varepsilon\sum_{j=1}^{M}E_j^{\rm pool},
\qquad a,b,\varepsilon>0.
\tag{1.4}
$$
固定 $q\ge0$，假定
$$
M\ge2q+4.
\tag{1.5}
$$
使用该有限模型的原头、孔层和联合旗，窗口宽度为 $4$。
记真正左、裸右、完整右费用为 $\mu,\alpha,\lambda$，
相应左、完整右源 Gram 为 $J,G$，并置
$$
r^\flat=GJ^{-1}r.
$$
各最小化与源空间均按既有四矩框架定义，不把构造原像直接称为极小者。

令
$$
s_0=\sqrt{a^2+b^2},\qquad \nu\ge\|D\|,\qquad
C_\star=13\left(\nu+s_0^{-1}\right).
\tag{1.6}
$$

**结论。** 对全部同返回源规范状态
$a^\sharp\perp_{I+\mathcal Q}\ker B_A$，
$$
\boxed{\mu(\mathsf f a^\sharp)\le C_\star\|a^\sharp\|.}
\tag{1.7}
$$
对整个第 $q$ 孔源空间中的任意源，
$$
\boxed{
\mu(r)\le(2C_\star+1)\alpha(r)
 +(C_\star+1)\lambda(r^\flat).
}
\tag{1.8}
$$
因此
$$
\boxed{
\mu(r)^2\le
(5C_\star^2+6C_\star+2)
\bigl(\alpha(r)^2+\lambda(r^\flat)^2\bigr).
}
\tag{1.9}
$$
常数不依赖 $q$、$M$、池小权 $\varepsilon$ 或头小 carry $\eta$，
只保留 (1.6) 中真实的异常权下界与尾范数上界。

## 2. 全池的正交串，及唯一有高返回的源块

对等权池作完整正交原始串分解。
每个池原始向量的出生为 $j$，其串长参数为
$$
L_j=M-2j.
$$
它张量两个异常位后，尾原始出生只能为
$$
j,\quad j+1,\quad j+2.
\tag{2.1}
$$
这是整个池 Hilbert 空间的正交分解，包含全部原始向量的重数；
并非只取置换不变的一条串。

为直接检查 (2.1)，把每条池串等距识别为 $L_j$ 个等权位的对称串，
两个异常位保留。令 $\Phi_{F,p}$ 为第 $p$ 个相对孔层的加权矩向量，
其集合系数是权乘积乘以指标函数 $1_{\{F\subset I\}}$，
其中 $F\subset\{1,2\}$。这些向量张成该层（上端可有线性关系），且逐集合计数给
$$
D^*\Phi_{F,p-1}=(p-|F|)\Phi_{F,p}.
$$
对 $p\ge3$，全部系数非零；每个非零目标矩向量都在这个像内，
其前一层矩向量也存在。因此 $D^*$ 到第 $p$ 层满射，
即 $D$ 从第 $p$ 层删除时单射。
这个论证包含维数减少的最后两层，没有把中段四维公式外推。
所以 primitive 只能在相对 $0,1,2$ 层出生，给出 (2.1)。
在 (1.5) 下，所有本稿源及修补涉及的 $j\le q$ 块满足
$L_j\ge4+2(q-j)$，所用层均有完整四矩余量。

池串及其副本约化 $D,D^*$；因此也约化所有尾核旗、
头张量算子、左右链约束、最小逆与源 Gram。
不同块的所有费用准确作正交平方和。

原高输出要求绝对出生至少为 $q+2$。
源孔数为 $q$ 又要求池出生 $j\le q$。
若 $j<q$，(2.1) 给该块最高出生至多 $q+1$，
所以其高输出空间为零，准确有
$$
B_A=0,\qquad \lambda=\alpha.
\tag{2.2}
$$
在这些块上，同返回源的 $I+\mathcal Q$ 最小者只能为零。

因此 (1.7) 只须处理 $j=q$ 的所有正交副本。
这里
$$
L=M-2q\ge4,
$$
而整个首源尾层都是一个相对真空。
这正是已付四矩约化中唯一可能产生高返回的块。

## 3. 相对真空的准确首层 Gram

固定其中一个单位相对真空 $\Omega_q$。
从相对一孔层删除到该真空的三个正交坐标，
分别是两个异常位与池的第一升阶向量。
删除行准确为
$$
(a,\ b,\ \varepsilon\sqrt L),
$$
所以
$$
\boxed{s^2=a^2+b^2+L\varepsilon^2.}
\tag{3.1}
$$
这里是约化串的 $L$，不是整个池的 $M$。

这个首层删除的 Moore–Penrose 逆为
$$
R\Omega_q=s^{-2}D^*\Omega_q,\qquad
\|R\Omega_q\|^2=s^{-2}.
\tag{3.2}
$$
由于池串约化 $D,D^*$，从其他串或其他副本取输入不可能降低该源的最小范数。
所以 (3.2) 也是完整有限尾上的相同源最小逆。

令 $k$ 只有第一段 $e_0R\Omega_q$ 非零。
它满足原联合旗，首源为 $e_0\Omega_q$，所有内部输出为零，
并且任何同源链的第一段第零头都必须解该删除方程。
因此它同时是真裸最小链和完整最小链，并有
$$
k\in\ker B_A,\qquad \|k\|=s^{-1}.
\tag{3.3}
$$

取该块任意裸状态 $a^\sharp$，源写为
$r=r_0e_0+r_1e_1+r_2e_2$，省略固定真空。
因第一段各头的删除行都是 (3.1)，
$$
\boxed{\|r\|\le s\|a^\sharp\|.}
\tag{3.4}
$$
最低头的精确分离还给
$$
\langle a^\sharp,k\rangle=r_0/s^2.
\tag{3.5}
$$
这是首段原像的正交性，不使用一个高孔统一逆范数。

## 4. 原长跳跃重建全部左质量

这个相对真空源块的左输入只有第 $q$ 孔层。
其左最小者恰为
$$
v=v_1e_1+v_2e_2+v_3e_3,\qquad r=Av,\qquad
\mu(r)=\|v\|.
\tag{4.1}
$$
理由同四矩三 Gram 字典：左零源的顶端头在 $\ker A=\mathbb Ce_0$，
而 (4.1) 与它正交。没有其他非零左层。

由 (1.1)，
$$
r_0=v_1+\beta v_2+\gamma v_3,\qquad
r_1=\eta v_2+\beta v_3,\qquad
r_2=v_3.
\tag{4.2}
$$
纯首头源 $e_0\Omega_q$ 的左最小者是 $e_1\Omega_q$。
所以同返回源规范对 (3.3) 的正交给
$$
\boxed{v_1=-r_0/s^2.}
\tag{4.3}
$$
此处正负号由
$\langle a^\sharp,k\rangle+\langle v,e_1\Omega_q\rangle=0$
直接确定。

记 $\alpha=\|a^\sharp\|$。
由 (3.4)、(4.2)、(4.3)，
$$
|v_1|\le\alpha/s,\qquad |v_3|\le s\alpha,
$$
$$
\beta v_2=-(1+s^2)v_1-\gamma v_3.
$$
因此在一般 $\beta\ne0$ 的四头形式 (1.1) 中已得到
$$
\boxed{
\mu(r)^2\le
\left\{
s^{-2}+
\left(\frac{1+s^2}{|\beta|s}
 +\frac{|\gamma|s}{|\beta|}\right)^2+s^2
\right\}\alpha^2.
}
\tag{4.4}
$$
小的中间边权 $\eta$ 没有被反演；支付关键是实际非零长跳跃 $\beta$。

对两个实际头，(1.3) 给
$$
|v_2|\le(8/s+9s)\alpha,
$$
故
$$
\mu(r)^2\le(129s^{-2}+163s^2)\alpha^2
\le169(s+s^{-1})^2\alpha^2.
\tag{4.5}
$$
又由完整有限尾的真空测试，
$$
s_0\le s,\qquad
s^2\le a^2+b^2+M\varepsilon^2
=\|D^*\Omega_{\rm all}\|^2\le\nu^2.
$$
所以 (4.5) 给 $\mu(r)\le C_\star\alpha$。

每个 $j=q$ 副本的常数完全相同，
其余 $j<q$ 块的规范态由 (2.2) 为零。
对全部正交块作平方和，不付副本数或串数因子，便得到 (1.7)。

## 5. 从规范类到全部源的三 Gram

这一节只使用已经发表的规范校正机制，不重计为新投影定理。
对任意裸状态 $a$，取同 $B_Aa$ 的规范者 $a^\sharp$，
写 $e=a-a^\sharp\in\ker B_A$，并记
$$
\delta=\|e\|_{I+\mathcal Q}.
$$
原完整状态度量 $\mathcal P=I+\mathscr L$ 在 $\ker B_A$ 上为 $I$，
且
$$
\lambda(r^\flat)=\|\mathcal P^{-1/2}\mathcal Qa\|.
$$
规范正交和两次 Cauchy--Schwarz 准确给
$$
\delta\le\alpha(r)+\lambda(r^\flat).
\tag{5.1}
$$
因为 $I+\mathcal Q$ 同时控制裸范数和左费用，
$$
\begin{aligned}
\mu(r)
&\le\mu(\mathsf f a^\sharp)+\delta\\
&\le C_\star(\alpha(r)+\delta)+\delta\\
&\le(2C_\star+1)\alpha(r)
 +(C_\star+1)\lambda(r^\flat).
\end{aligned}
$$
这证明 (1.8)；二维 Cauchy--Schwarz 给 (1.9)。

若写成原源 Gram，(1.9) 等价于
$$
J^{-1}\le
(5C_\star^2+6C_\star+2)
\bigl(J_{\rm bare}^{-1}+J^{-1}GJ^{-1}\bigr).
\tag{5.2}
$$
所有逆均为原全部源块上的真实逆，次序保持不变。

## 6. 原模型的应用边界

若用 $m$ 仅标记一个外部尾尺度，并有 $a,b\ge c(m+2)^{-2}$，且整个有限尾满足
$\|D\|\le C/m$，则 (1.6) 的 $C_\star=O(m^2)$，
三 Gram 常数为 $O(m^4)$。
这是该有限四头模型内的真实成本；这里没有把头维数改成 $2^m$，也不把池的相对真空换成原一般高孔向量。

本稿将旧十一位 $q=1$ 规范结果扩到另一种完整有限尾结构：
任意 $q$、任意允许池重数、独立尾小权和头小 carry，
并保留两个实际四头的长跳跃。
它没有证明原非等权连续尾能按同样方式只留下一个相对真空返回块，
也没有把四头的两条源行重建移到一般 $d=2^m$。
这些是继续拼回原无权来源时必须支付的部分。
