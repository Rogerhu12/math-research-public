# 真核的集体占据矩与单个物理位旋转：费用不含总孔数

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；旋转和占据预算由 boundary_core 与 root 共同推进。AI-assisted，GPT-6 Astra Pro。

**状态：已证明的中间结论。** 本稿接续[全出生真核的零占据重构](2026-11-14-full-boolean-kernel-bosonic-zero-occupation-and-head-only-budget-789f-next.md)。在原 \(A_m\) 下，真实核不仅只有有限集体占据，其平均占据至多 \(k_0=\max(2m,16)\)，第二矩至多 \(k_0^2\)，全部高占据尾有显式四次指数界。加入一个真实物理位时，完整 bosonic 模式旋转的导数因而只付 \(O(\sqrt m)\)，不含总孔数或 primitive 出生数。

旋转一般不保持原平方自由空间；末节只给实际硬核距离的上界，不把距离小改称存在同源物理核提升。

## 1. 原头、尾行与准确集体占据

取原 \(N/Y\) 有限头 \(A_m\)、\(d=2^m\)、\(m\ge5\)。本稿允许尾从 \(m\) 或 \(m+1\) 开始，也允许在这样的行上再添正权物理位。其平方和 \(S\) 因而至少满足
\[
S\ge \frac1{3(m+2)^3}.
\tag{1.1}
\]
取完整集体模式 \(a_0=D/\sqrt S\)（右侧在原平方自由子空间上理解；在完整 Fock 空间中用相应闭 annihilator），并记
\[
N_0=a_0^*a_0,\qquad k_0=\max(2m,16),\qquad
\gamma=\frac{770}{16^4}>\frac1{100}.
\]

对任何真实平方自由核向量
\[
v\in\ker(A_m+D),
\]
前稿给 \(h=P_0v\) 及正交展开
\[
v=\sum_{j=0}^{d-1}|j\rangle_0\otimes
      \frac{(-A_m)^jh}{\sqrt{S^j j!}}.
\tag{1.2}
\]
因此
\[
\|v\|^2=\sum_j\frac{\|A_m^jh\|^2}{S^j j!},\qquad
\langle N_0^rv,v\rangle
=\sum_j j^r\frac{\|A_m^jh\|^2}{S^j j!}
\tag{1.3}
\]
对每个非负整数 \(r\) 都准确成立。特别这里已在真实闭域中，不能把环境无界算子的期望当作形式和。

## 2. 全出生的一阶、二阶矩及高占据尾

前稿保留的原头 carry 界为
\[
\|A_m^j\|\le6^j e^{-\gamma j^4}
\quad(j\ge k_0).
\tag{2.1}
\]
置 \(\tau=\log(36/S)\)。由 (1.1)，
\[
\tau\le \log108+3\log(m+2)\le3m
\qquad(m\ge5).
\]
同时 \(k_0^3\ge512m\)，故 \(\tau\le\gamma k_0^3\)。于是对全部 \(j\ge k_0\)，
\[
\frac{\|A_m^j\|^2}{S^j j!}
\le\frac{e^{\tau j-2\gamma j^4}}{j!}
\le\frac{e^{-\gamma j^4}}{j!}.
\tag{2.2}
\]

对 \(r=1,2\)，分别使用
\[
\sum_{j\ge0}\frac{j}{j!}=e,\qquad
\sum_{j\ge0}\frac{j^2}{j!}=2e
\]
可得
\[
\sum_{j\ge k_0}j^r
 \frac{\|A_m^jh\|^2}{S^j j!}
\le 2e\,e^{-\gamma k_0^4}\|h\|^2
<\|h\|^2.
\tag{2.3}
\]
最后严格不等式由 \(k_0\ge16\)、\(\gamma>1/100\) 立即成立。

低占据部分分别至多
\((k_0-1)\|v\|^2\) 和 \((k_0-1)^2\|v\|^2\)，而 \(\|h\|\le\|v\|\)。所以
\[
\boxed{
\langle N_0v,v\rangle\le k_0\|v\|^2,\qquad
\langle N_0^2v,v\rangle\le k_0^2\|v\|^2.
}
\tag{2.4}
\]
对任意整数 \(K\ge k_0\)，还准确有
\[
\boxed{
\|1_{[K,\infty)}(N_0)v\|^2
\le e^{\,1-\gamma K^4}\|v\|^2.
}
\tag{2.5}
\]
证明是将 (2.2) 从 \(K\) 起求和，并用
\(\sum1/j!=e\)、\(\|h\|\le\|v\|\)。

所有常数均独立于总物理孔数、横向 Fock 次数、出生数和源维数。没有用碰撞概率小或低孔截断。

## 3. 单个真实物理位的完整旋转生成元

现把一条旧尾与一个新物理位作张量积。记旧集体 annihilator 为 \(a_0\)，新位的完整 bosonic annihilator 为 \(c\)。它与旧尾所有算子交换。定义
\[
\mathsf G=c^*a_0-a_0^*c,\qquad U_\theta=e^{\theta\mathsf G}.
\tag{3.1}
\]
这是两正交一粒子模式旋转的第二量子化酉群，且
\[
U_\theta a_0U_\theta^*
=\cos\theta\,a_0+\sin\theta\,c.
\tag{3.2}
\]
先在有限两模式占据子空间计算，再用该酉群的闭生成元延拓；以下实际向量均在所需域中。

任何新位平方自由向量都可写为
\[
v=v_0\otimes|0\rangle_c+v_1\otimes|1\rangle_c.
\]
直接作用生成元：
\[
\mathsf Gv
=(a_0v_0)\otimes|1\rangle_c
+\sqrt2(a_0v_1)\otimes|2\rangle_c
-(a_0^*v_1)\otimes|0\rangle_c.
\tag{3.3}
\]
三个输出的新位占据互相正交。由完整 CCR，
\(\|a_0^*v_1\|^2=\|a_0v_1\|^2+\|v_1\|^2\)，故
\[
\boxed{
\|\mathsf Gv\|^2
=\|a_0v_0\|^2+3\|a_0v_1\|^2+\|v_1\|^2
\le3\|a_0v\|^2+\|v\|^2.
}
\tag{3.4}
\]
这一步没有出现总孔数 \(q\)。一般两模式估计中的 \(q\) 被真实新位占据至多 \(1\) 的条件消去。

若 \(v\) 是旧真实核向量张量新位真空，则 \(v_1=0\)，(2.4) 进一步给
\[
\boxed{\|\mathsf Gv\|^2
=\langle N_0v,v\rangle\le k_0\|v\|^2.}
\tag{3.5}
\]

## 4. 对新真实核也有不含总孔数的界

设旧行平方和为 \(S\)，新物理权为 \(a>0\)，置
\[
t=\frac{a^2}{S},\qquad
S_+=S+a^2,\qquad
a_+=\frac{\sqrt S\,a_0+a c}{\sqrt{S_+}}.
\]
考虑同一实际头的新平方自由核
\[
(A_m+D_{\rm old}+aE_{\rm new})v=0.
\]
完整 Fock 中它满足
\((A_m+\sqrt{S_+}a_+)v=0\)。
因为 \(S_+\ge S\)，§2 的同一 \(k_0\) 占据界继续适用：
\[
\|a_+v\|\le\sqrt{k_0}\|v\|.
\]
新位的物理条件给 \(\|cv\|\le\|v\|\)。由准确身份
\[
a_0=\sqrt{1+t}\,a_+-\sqrt t\,c
\]
得到
\[
\|a_0v\|
\le\bigl(\sqrt{(1+t)k_0}+\sqrt t\bigr)\|v\|.
\]
代入 (3.4)，
\[
\boxed{
\|\mathsf Gv\|^2
\le
\left[3\bigl(\sqrt{(1+t)k_0}+\sqrt t\bigr)^2+1\right]\|v\|^2.
}
\tag{4.1}
\]
此处旧模式 \(a_0\) 与新集体模式 \(a_+\) 没有混同。

对 (3.5) 或 (4.1) 中任意一个实际向量，酉群及 \(\mathsf G U_\theta=U_\theta\mathsf G\) 给
\[
\boxed{\|(U_\theta-I)v\|\le|\theta|\,\|\mathsf Gv\|.}
\tag{4.2}
\]
这个整弧估计只需原始向量的生成元范数；不要求旋转过程中仍平方自由。

## 5. 旧核加真空的实际硬核距离是二阶

设 \(v\) 是旧平方自由真核，补上新位真空。令 \(Q_{\rm hc}\) 为包含新位在内的完整平方自由正交投影。由 (3.3)，
\[
v\in\operatorname{Ran}Q_{\rm hc},\qquad
\mathsf Gv=(D_{\rm old}v/\sqrt S)\otimes|1\rangle_c
\in\operatorname{Ran}Q_{\rm hc}.
\tag{5.1}
\]
第二式使用真实删除保持平方自由性。

再作用一次，得到两个正交新位输出：
\[
\mathsf G^2v
=\sqrt2\,a_0^2v\otimes|2\rangle_c
-N_0v\otimes|0\rangle_c.
\]
因此
\[
\|\mathsf G^2v\|^2
=3\langle N_0^2v,v\rangle-2\langle N_0v,v\rangle
\le3k_0^2\|v\|^2.
\tag{5.2}
\]
酉群的二阶积分余项和 (5.1) 给
\[
\boxed{
\|(I-Q_{\rm hc})U_\theta v\|
\le\frac{\theta^2}{2}\|\mathsf G^2v\|
\le\frac{\sqrt3}{2}\,k_0\theta^2\|v\|.
}
\tag{5.3}
\]
该界控制到原硬核空间的距离，并不提供到某个新核交集的距离。

## 6. 与新增位 graph 的明确边界

本稿保留以下两个实质区别：

1. \(U_\theta\) 是完整 bosonic 酉旋转。即使 (5.3) 很小，投影 \(Q_{\rm hc}U_\theta v\) 一般也不再满足所需核方程；annihilation 可把重复占据送回平方自由层，因此不能把 \(Q_{\rm hc}\) 与它交换。
2. 当 \(\tan\theta=a/\sqrt S\) 时，(3.2) 的模式方向是新集体模式，但
   \[
   U_\theta(A_m+\sqrt S\,a_0)U_\theta^*
   =A_m+\sqrt S\,a_+
   \]
   的总强度仍为 \(\sqrt S\)，而实际新核用 \(\sqrt{S_+}\)。完整比较还必须保留这个同一头的强度变化；不能仅凭模式方向相同就声称交织了新物理方程。

因此新增位的真实 \(K_\perp\)、完整旧核投影、未来 bare 类与 flat 度量仍需原问题中的可行提升。本稿新增的是全出生真实占据矩、四次尾、无总孔数的旋转费用，以及 (5.3) 的二阶硬核距离；普通 ISP、\(N=M\) 和原两费比较仍开放。
