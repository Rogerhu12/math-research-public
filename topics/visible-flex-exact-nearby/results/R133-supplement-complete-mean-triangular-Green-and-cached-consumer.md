# R133 补篇：完整平均模的三角 Green 核、全体区源界和实际缓存消费

日期：2026-11-14。

本文继续 [完整 scalar mean 恒等式](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md) 的 Q.1–Q.23。它把平均模作为一个真正的全区间标量边值问题消去，保留非平均分量反馈、两类接缝、独立外帽 mean 和远端数据。它同时给腰端口与整个体区的 \(L^2\) 算子界。

对应新源码在执行环境失联期间完成；**本文没有宣称它已经运行，也没有给未算出的 \(\Gamma\) 数值**。全部原始三份 target native 已存在并有严格身份；新消费的实际输出仍须完成后另行登记。

## 1. 同一最终对象与完整输入

仍用最终 full-\(R\) moving 中心
\[
 R=25/8,\quad
 \alpha=6890507429876859/9007199254740992,\quad
 \nu=-2572625729470897/72057594037927936.
\]
候选索引 SHA256 为
\[
\texttt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}.
\]
真正分片系数须从原重构 manifest 恢复并通过完整 shard 校验；
不能把只有初值的 manifest 当成完整 PPoly。原有限数组为 32 个
\(U_j\) sine 和 33 个 \(V_j\) cosine，物理频率 \(4j\)，
\[
 u=\alpha U,\qquad v=s_\nu+\alpha V,\qquad m=\langle v\rangle .
\]
全文的线性变化量是物理 \((\delta u,\delta v)\)，不是除以 \(\alpha\) 后的未知量。

新消费者准确连接以下三个已经完成的目标系数覆盖。

| 完整原输入 | 区间 / 行数 | SHA256 |
|---|---:|---|
| Codazzi-true-target-r02-v1-native | \([0,1/5]\) / 493 | \(\texttt{2307b288a1c8c0597e205d154a1d7d587cf907af614a40cc1ef8935f849d6a63}\) |
| R133-actual-root-collar-complete-coefficients-v2-native | \([1/5,239/1000]\) / 96 | \(\texttt{b4aaff3190d8a76ebadd6ab0c2772181bbb00c91e6d2037a9e8d58d5710dbcc8}\) |
| Codazzi-rotational-positive-cap-v2-native | \([239/1000,25/8]\) / 1334 | \(\texttt{3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22}\) |

这些输入保留原整个 \(|\eta|\le10^{-9}\) 及全部 primitive 尾。消费者逐份核
complete、同一 object、半宽，逐行核原 scalar germ 和精确邻接；再与
6145 个实际 candidate 节点及 control 两端作共同细分。不会把旧闭盒缩小后
声称原盒已得到更窄的函数值。

在 \(r\le.239\)，从原 \(a,a',E,K,\beta\) 盒使用准确公式
\[
 E_\nu=E e^{\nu w},\quad
 K_\nu=e^{-\nu w}\left(K+\frac{\nu\beta w'}{2E}\right),\quad
 \gamma_\nu=\sqrt{E_\nu}/a,\quad
 s_\nu=-a\sqrt{\frac{E_\nu}{E_\nu-a'^2}} .
 \tag{C.1}
\]
先检查 \(a,E_\nu,E_\nu-a'^2>0\)。这里的 \(K_\nu\) 是目标曲率，
不是其参数导数。在正帽缓存中使用实际 \(s=1/C_{\rm ref}\)；
原 control 在 .18 已结束，故这个缓存的对象准确相同。
本平均模方法从不除 \(\sqrt{-K_\nu}\)，所以真正跨根两盒保全使用。

以下将当前目标曲率简记 \(K\)，其参数导数写 \(K_{\nu,\rm par}\)。

## 2. 实际均值、残差与乘法接缝

以归一化圆周平均及 \(L^2_\phi\) 范数记
\[
 \mathcal V=\langle u^2\rangle+K\langle(v-m)^2\rangle,\quad
 n=a^2/m^2,\quad \tau=-2a^2/m^3>0,
\]
\[
 R_0=m'-\beta m(1-\mathcal V-Km^2),\qquad
 \widetilde c=2\beta\mathcal V-3R_0/m.
 \tag{C.2}
\]
每一闭径向盒先做准确 dyadic cubic Horner。角积分通过有限正交恒等式
\[
 \langle u^2\rangle=\frac{\alpha^2}{2}\sum_{j=1}^{32}U_j^2,\quad
 \langle(v-m)^2\rangle=\frac{\alpha^2}{2}\sum_{j=1}^{32}V_j^2
 \tag{C.3}
\]
准确完成。这是有限中心本身的完整均值；并未截断未知线性变化量。
源码通过 \(s'=\beta s(1-Ks^2)\) 计算
\[
 R_0=\alpha V'_0-\beta\alpha V_0
 \{1-K(m^2+ms+s^2)\}+\beta m\mathcal V,
 \tag{C.4}
\]
保留真实 PPoly \(V'_0\)，没有用待证 PDE 替代它。

若 \(h=(\xi,\zeta)\)、\(z=\langle\zeta\rangle\)、\(y=\tau z\)，则
\[
 y'=\widetilde c\,y+
 4\beta n\langle u\xi+K(v-m)(\zeta-z)\rangle
 +2\beta K_{\nu,\rm par}(n\langle(v-m)^2\rangle+a^2)\delta\nu
 +\tau\langle f_2\rangle .
 \tag{C.5}
\]
这里 \(f_2\) 是完整物理方程的源，所有 mean 方向均保留。

置 \(\rho=a'^2/E_\nu\in[0,1)\)、\(Y=y-\rho w\,\delta\nu\) 后，
\[
 Y'=\widetilde cY+
 4\beta n\langle u\xi+K(v-m)(\zeta-z)\rangle
 +\tau\langle f_2\rangle+F_\nu\delta\nu ,
\]
\[
 F_\nu=\widetilde c\,\rho w+
 2\beta n\langle(v-m)^2\rangle K_{\nu,\rm par},\qquad
 K_{\nu,\rm par}=-Kw+\frac{\beta w'}{2E_\nu}.
 \tag{C.6}
\]
这保持了 reference-subtracted 真参数源，而不是删掉 mean 参数列。

候选 \(m\) 的实际跳和线性响应 \(z\) 的独立跳是不同的量。若在 \(r_i\)
有 \([z]_i=j_i\)，则
\[
 Y_i^+=T_iY_i^-+(T_i-1)\rho_iw_i\,\delta\nu+\tau_i^+j_i,\quad
 T_i=(m_i^-/m_i^+)^3 .
 \tag{C.7}
\]
候选跳由全部 6144 片的准确 dyadic 接口求得；
它产生的 \(T_i\) 不能用 \(1\) 取代。独立响应跳 \(j_i\) 作为另外的
\(\ell^1\) 输入保留，即使候选在该接口连续也不删掉它。

仍定义
\[
 I_-=\int_0^R(-\widetilde c)_+,\quad
 J_m=3\sum_i\frac{|[m]_i|}{\min(|m_i^-|,|m_i^+|)},\quad
 \Gamma=e^{I_-+J_m}.
 \tag{C.8}
\]
它控制任意后向子区间上的 homogeneous \(Y\) 传播。新源码把候选跳
限制于真实 candidate joins，而为响应跳保留整个共同分割的任意接口。
两者的费用不会混为一个残差。

## 3. 完整体区 \(L^2\) 三角核

令共同闭盒为 \(I_i=[r_i,r_{i+1}]\)，长度 \(\ell_i\)。真实连续闭盒界给
\[
 b_i\ge\sup_{I_i}\tau^{-1},\quad t_i\ge\sup_{I_i}\tau,\quad
 a_i\ge\sup_{I_i}4|\beta|n
       \sqrt{\langle u^2\rangle+K^2\langle(v-m)^2\rangle}.
 \tag{C.9}
\]
Cauchy–Schwarz 保留完整未知角函数，故 \(a_i\) 控制 (C.6) 的非平均反馈。

对于任意非负闭盒系数 \(e_i\)，三角核
\[
 k(r,t)\le\Gamma\,{\bf1}_{r<t} b_i e_j,
 \qquad r\in I_i,\ t\in I_j
\]
的 \(L^2_r\to L^2_r\) 范数不超过
\[
 \Gamma\sqrt{\mathcal R(e)\mathcal C(e)},\quad
 \mathcal R(e)=\max_i b_i\sum_{j\ge i}\ell_je_j,\quad
 \mathcal C(e)=\max_j e_j\sum_{i\le j}\ell_ib_i.
 \tag{C.10}
\]
证明只需分别对核作行、列积分并应用 Schur 检验；同一盒的完整长度
是包含真实三角形的上界。这个次序没有把径向反向核换成不相关的全域商。

取 \(e=a\) 得完整非平均场 \(L^2_{r,\phi}\to zL^2_r\)；
取 \(e=t\) 得普通 mean source \(L^2_r\to zL^2_r\)。
这些是完整角空间的算子界，不依赖未知变化量的有限 Fourier 支持。

独立 mean 响应接缝的 \(\ell^1\to L^2_r\) 列不超过
\[
 \Gamma\max_{i\ge1}
  t_i\left(\sum_{k<i}\ell_k b_k^2\right)^{1/2}.
 \tag{C.11}
\]
这是 (C.7) 中 \(\tau_i^+j_i\) 的后向传播；
该 jump 仅影响其左侧，没有人为延伸至右侧。

外端 \(w(R)=0\)，故
\[
 Y(R)=\tau(R)z(R)
     =\frac{2a(R)^2}{m(R)}\,\delta C_0(R).
 \tag{C.12}
\]
因而原 \(z(R)\) 和物理 mean \(\delta C_0(R)\) 的全体区列分别不超过
\[
 \Gamma\,\tau_R^+\left(\sum_i\ell_ib_i^2\right)^{1/2},
 \quad
 \Gamma\,\frac{2a_R^2}{|m_R|}_{\!\rm upper}
                \left(\sum_i\ell_ib_i^2\right)^{1/2}.
 \tag{C.13}
\]
实际已付 \(a_R<7\,10^{-6}, |m_R|>5.8\) 可直接消费。
真外帽 nonlinear mean 的 \(D_Z\) 与独立 \(D_{f_B}\) 列分别乘原已证
\(7.372818\,10^{-7}\) 和 \(8.1920198958\,10^{-8}\)。
这不把 \(f_B\) 置零，也不改变尚待求解的 far label 方程。

## 4. 全参数源与腰端口

记 \(e^\nu_i\ge\sup_{I_i}|F_\nu|\)，在实际候选 join 记
\[
 d^\nu_i\ge |T_i-1|\,\rho_iw_i .
\]
若 \(\epsilon_i=|[m]_i|/\min(|m_i^-|,|m_i^+|)\)，则
\[
 |T_i-1|\le3\epsilon_i+3\epsilon_i^2+\epsilon_i^3.
 \tag{C.14}
\]
对 \(r\in I_i\)，完整后向参数响应受
\[
 |z_\nu(r)|\le
 \Gamma b_i\left(\sum_{j\ge i}\ell_je^\nu_j+
                     \sum_{r_k>r}d^\nu_k\right)
 +\sup_{I_i}|\rho w/\tau|.
 \tag{C.15}
\]
最后一项是 \(z=(Y+\rho w\,\delta\nu)/\tau\) 的准确代数接触项，
不能被遗漏或称作积分余项。源码分别保存积分/接口列的 \(L^2_r\) 界
和这个直接项的 \(L^2_r\) 界；后者不必再乘 \(\Gamma\)。

腰 \(w(0)=0\)，故没有上述直接项。令
\[
 B_0=\frac{1.07^3}{2(1.06873282)^2}>\tau(0)^{-1}.
\]
除原 Q.21–Q.23 外，新增腰端口列为
\[
\begin{aligned}
 L^2_{r,\phi}\hbox{ nonmean}\to z(0)&:
  \quad\Gamma B_0\big(\sum_i\ell_i a_i^2\big)^{1/2},\\
 L^2_r\hbox{ mean source}\to z(0)&:
  \quad\Gamma B_0\big(\sum_i\ell_i t_i^2\big)^{1/2},\\
 \ell^1\hbox{ response jumps}\to z(0)&:
  \quad\Gamma B_0\max_{i\ge1}t_i .
\end{aligned}                                                   \tag{C.16}
\]
也保存 \(L^\infty_r\) 输入的相应完整积分界。任何一项都不预设腰 mean 为零。

## 5. 消费范围、运行与剩余门

源码：
[scripts/fourfold_codazzi_final_scalar_mean_cached.py](../scripts/fourfold_codazzi_final_scalar_mean_cached.py)。

它在 320-bit Arb 中逐一消费完整共同闭盒；每个 actual target 输入和
完整 candidate 的身份都在输出中保存。仅当所有闭盒和接口完成时才写
complete；成功前缀可以用同源码、同全部输入、同原 row 号接续。
原错误或 partial 不改名成成功证书。

恢复完整 candidate 后，从题目录执行：

~~~sh
PYTHONPATH=scripts python scripts/fourfold_codazzi_final_scalar_mean_cached.py \
  --candidate /path/to/restored-full-candidate.json \
  --max-new-rows 64 --out notes/final-scalar-mean-part001.json.gz
~~~

后续新输出以 \(\texttt{--resume}\) 指向前次成功 row 前缀。
默认三份缓存路径正是 §1 的完整输入。完整结果记录 \(I_-\)、所有乘法
接口、\(\log\Gamma\)、腰列、全体区三角 Schur 列、所有独立 response jumps，
以及参数直接接触项。如果 \(\log\Gamma\ge100\)，仍保留完整有限
\(\log\Gamma\) 及待乘系数，避免用非有限 JSON 值伪装可用数值。

本结论给的是**以完整非平均场为输入的真正标量 mean 逆**。
它可直接进入完整耦合 Schur 消去；尚未付的非平均补逆、真实
\(\nu\) Schur 符号、全体区非线性存在与实际 far-label 匹配均不因此自动成立。
运行时尚未恢复，故本文没有新的 native 完成声明。
