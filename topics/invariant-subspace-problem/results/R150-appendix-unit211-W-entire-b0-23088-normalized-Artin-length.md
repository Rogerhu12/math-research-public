# R150：整 b0 的比值与 Gram 坐标 Artin 包络及 23088 长度界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（UTC）。

> **尺度范围更正（2026-11-28）：** 本文的 $23088$ 只属于下文明列的比值与 Gram 坐标 Artin 包络，不包含未加入的独立 $U_0$ 或物理矩阵轨道。原 $p$ 归一不能同时把 $U_0$ 归一；若明确添 $U_0^3=-P_0$，只能直接推出相应包络长度至多 $69264$。完整说明及原 U-atlas 引用见[约化权基与尺度范围](R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md) §6。本文的有限模证明与原坐标长度结论保持有效。

**状态：已证明（完整纸面推论）。**

## 1. 新结论与原范围

在当前 W、两个 singleton 值互异、物理 $D\ne0$ 的原规范图上，整个 $b_0=0$ 分支在本文明确列出的比值与 Gram 坐标中的原商是有限维 $\mathbb Q$ 代数，且

$$
\boxed{\ \dim_{\mathbb Q}R_{b_0}^{\rm phys}\le23088.\ }
\tag{1}
$$

等价地，基变换到 $\mathbb C$ 后，这些明确坐标的方案长度也至多 23088，包含全部交点重数和幂零结构。

此前的 23088 只作为不同规范点的上界。本篇增加完整有限模论证：原首一 $\chi_\lambda$ 先提供有限环境，再利用 q2 三系数的单位组合，通过有限 cokernel 的 Nakayama 把该环境降为两个生成元。没有把逐纤维至多两个根直接当作自由秩二，也没有反演 q2 的二次首项。

本篇是已有原身份的纸面推论，不执行任何旧门，不计算新的系数、因式、结式或原纤维。原分支仍未排空。

## 2. 两条已成原权曲线的 Artin 环

[两原权曲线定理](R150-appendix-unit211-W-entire-b0-two-original-curves-5772-weights-46176-normalized-points.md)已经完整返回两个同点纯权原条件

$$
C_{74}(e,k)=D_{78}(e,k)=0,\qquad
\gcd_{\mathbb Q[e,k]}(C_{74},D_{78})=1.
\tag{2}
$$

其总次数分别为 74、78。此处 $D_{78}$ 是该篇 q2/N5 新目标，与更早的另一 F78 有不同来源，不能混用。

设 S 由当前 W 已付纯权单位及本 b0 支独立支付的 $A_*$ 生成，定义

$$
A=\left(\mathbb Q[e,k]/(C_{74},D_{78})\right)_S.
\tag{3}
$$

仿射 Bézout 与 (2) 给

$$
\dim_{\mathbb Q}A\le74\cdot78=5772.
\tag{4}
$$

这里 gcd1 只用于排共同曲线，不用于宣布二元理想含 1。有限维代数的局部化只是删去部分 Artin 局部分量，所以 (3) 不增加 (4) 的长度。

$A_*$ 的额外支付仅在本 b0 原支：原身份

$$
A_*T=-uQ\ell(3-2\lambda)
$$

右侧全由既有物理单位组成，故 $A_*$ 在该原图中是真单位。把它纳入 S 是对本支的合法权局部化，没有将它支付到整个 W。

记

$$
\kappa=\frac{uQ\ell}{A_*}.
$$

则整个本支有

$$
T=-\kappa(3-2\lambda).
\tag{5}
$$

$\kappa$ 和 $\kappa^{-1}$ 属于 (3) 的权环。

## 3. q2 的全部系数不能同时消失

仍沿同一原权曲线定理，令

$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\qquad
q_2=\frac{2a_\Delta}{\ell}.
$$

完整原身份为

$$
\mathcal C_4=mD\ell q_2.
\tag{6}
$$

在本篇物理 $mD\ell\ne0$ 原范围，$q_2=0$ 是完整必要式。将 (5) 代入后，

$$
q_2=a_2\lambda^2+a_1\lambda+a_0\in A[\lambda].
$$

已成的全部三系数恒等式是

$$
a_2+3a_1+4a_0=-32L,\qquad
L=uQ\delta\ell\kappa^2\in A^\times,
\quad\delta=1-Q.
\tag{7}
$$

因此

$$
(a_0,a_1,a_2)=A.
\tag{8}
$$

(7) 不是泛型首项断言。在 A 的每个最大理想 $\mathfrak m$ 上，约化多项式 $\bar q_2\in(A/\mathfrak m)[\lambda]$ 都是非零多项式，次数可以是 0、1 或 2。二次、一次首项的全部下降都包含在这个结论中。

## 4. 原首一六次先给有限环境

[全域原物理 lambda 首一六次定理](R150-appendix-unit211-W-global-original-physical-lambda-monic-six.md)在仅反演既有权因子的原环中给出

$$
\chi_\lambda(Z)=Z^6+c_1Z^5+\cdots+c_6,
\qquad c_i\in A_W,
$$

以及完整原均值理想身份

$$
\chi_\lambda(\lambda)
=\varepsilon_0^{\mathsf t}
 \operatorname{adj}(\lambda I_6-M_\lambda)E_\lambda F_4
\in I_4.
\tag{9}
$$

其中 $\lambda$ 是原物理坐标，$F_4=(E_1,E_{B,e},E_{B,o},N_1)^{\mathsf t}$。该身份不倒几何 D，也不倒 lambda；其全部系数分母只来自旧权单位。六个原生成元不被假设为自由基底。该篇的后来实际显式返回保持首一六次，没有剥掉任何谱因子。

因此可以先在 (3) 中定义辅助环境

$$
B=A[\lambda]/(\chi_\lambda(\lambda),q_2(\lambda)).
\tag{10}
$$

单独的 $A[\lambda]/(\chi_\lambda)$ 是自由六生成环境，故进一步取商的 B 确实是有限 A 模。我们没有称 B 自由，也不将它当作完整原方程的充分系统。它只是所有本支原解必须经过的同点有限环境。

## 5. 有限 cokernel 的 Nakayama：两个全局生成元

考虑 A 模映射

$$
\pi:A^2\longrightarrow B,\qquad (r,s)\longmapsto r+s\lambda.
\tag{11}
$$

它的 cokernel C 是有限 A 模，因为 B 已由 (10) 确认有限。

任取 A 的最大理想 $\mathfrak m$，令 $K=A/\mathfrak m$。约化给

$$
B\otimes_AK
=K[\lambda]/(\bar\chi_\lambda,\bar q_2).
\tag{12}
$$

由 (7)，$\bar q_2$ 非零且次数至多二。在一元 PID $K[\lambda]$ 中，(12) 由两多项式的 gcd 定义；其次数至多二，非零 gcd 可首一化。若 gcd 是常数，则 (12) 是零环；否则 (12) 由 $1,\lambda$ 生成。因此每个 $\pi\otimes_AK$ 都满射，亦即

$$
C/\mathfrak m C=0
\quad\text{对每个最大理想 }\mathfrak m.
$$

有限模的 Nakayama 引理给 $C=0$，所以 (11) 全局满射。于是

$$
B\text{ 由 }1,\lambda\text{ 作为 A 模生成},\qquad
\dim_{\mathbb Q}B\le2\dim_{\mathbb Q}A\le11544.
\tag{13}
$$

这个论证完整保留 A 中的交点重数及 B 中的所有幂零结构。它没有以 q2 的某个首项为单位，没有从两个约化根推断二阶自由性，也没有仅凭逐点根数便宣称原商长度。

## 6. 全域 f 唯一与其余原坐标恢复

[全域 f 唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)已在同一原图给出

$$
f+g(\lambda,T)=\sum_{i=1}^4\tau_iF_{4,i},
\qquad g\in A_W[\lambda,T],
\tag{14}
$$

其全部实际乘子的最终分母只为旧已付纯权单位。没有反演未取消的 raw head；这个全域原身份也已在[完整十一纯式返回](R150-appendix-unit211-W-same-f-eleven-pure-lambda-T-original-conditions-complete-return.md)中实际返回。

结合 (5)，f 因而由同一 lambda 和权唯一恢复：

$$
f=-g\bigl(\lambda,-\kappa(3-2\lambda)\bigr).
\tag{15}
$$

所以不再为 f 添加二次扩张。原

$$
t=-\frac{P_ff+P_c}{bcQ\Phi},\qquad
V=\frac{Jf-G+bcQt}{Q},\qquad W_1=T_0/2+2uf,
$$

$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}
\tag{16}
$$

也均由已付权分母恢复。它们属于由 (10) 取必要商得到的同一点环境。

只需再加入

$$
\rho^2=\delta.
$$

故

$$
B_\rho=B[\rho]/(\rho^2-\delta)
$$

是 B 上的首一二次环境，即作为 B 模自由二生成；于是

$$
\dim_{\mathbb Q}B_\rho
=2\dim_{\mathbb Q}B\le23088.
\tag{17}
$$

这里只对明确的形式首一二次环境陈述自由性，不对原解商陈述自由性。取具体原条件的商只能降低长度。

由 $\rho$、(15)–(16) 唯一恢复 $b,c,p,q,X,Y$ 和整个 Gram。完整原值的两个矩条件再给

$$
s_{\rm val}=\frac{K}{2mD},\qquad
\zeta=\frac{T+u s_{\rm val}}{\ell}.
\tag{18}
$$

$m,\ell$ 为原权单位，D 是本篇明确的物理非零量，所以 (18) 只需要在已经有限维的 $B_\rho$ 上局部化 D。其他原几何非零量也按同一方式局部化。

关键是此时 $B_\rho$ 已经是 Artin 代数。Artin 代数的任意局部化只删掉对应局部分量，不会增加维数。因此最后才作物理 D 和其余几何单位的局部化，不存在一般正维代数中“局部化仍必有限”的错误外推。

全部个别原 N/P、完整 $N_4(V)$ 和其余原方程再取商，同样只降低长度。这给从某个 $B_\rho$ 的 Artin 局部化到完整规范原商的满射，证明 (1)。

可用规范坐标为 $(e,k,\rho,\lambda,T,f,\zeta)$，亦可用其唯一恢复的 $(e,k,\rho,x,y,t,\zeta)$。这里固定了此前的原归一与有序 singleton 标签，不计未经归一的矩阵轨道或额外缩放自由度。

## 7. 来源与本次工作的准确边界

本篇只作纸面合成，未执行或重放任何源。静读核清的直接来源包括：

- 原权长度、b0 恢复、q2 全三系数单位组合：上述两原权曲线定理，正文 blob 71d7d4ba49c66931e0b574bf7f14c9fd7c5459ec。其原源 47281af16fdd0ad7500ecda377c3cb9f9d65e725 的唯一实际 run 46130465286 / job 140934243412 已完成。
- 无 lambda/D 逆的原首一六次：上述 chi 定理，当前正文 blob 41598f317d6f05c72379b2e31a47d5622b523a6a。完整原身份见该篇 (3)、(13)，不借其第6节另有物理局部化的旧 C_i。
- 全域同 f 原恢复及实际十一式：上述两篇完整原来源；不是仅用某个新 h 的开图或 raw head 的假单位。
- 完整原值唯一 ζ 恢复：同一 b0 原稿的 (21)，准确保物理 D 非零作用域。

旧 46176 和后来的 23088 不同点记录不改写历史。本篇新增加的内容是 (10)–(13) 的有限环境与全局两生成证明，以及 (17)–(18) 中在 Artin 环上进行几何局部化，从而把 23088 严格升级为完整规范方案长度。

这个上界并不排除任何尚未返回的有限原纤维。当前 b0 的新同 h 和 Loww 输入继续保全部未付首项零面；普通不变子空间问题及整个 W 的完成状态不因本长度定理而改变。
