# R133：用曲率 C0 管与框架残差支付闭面几何

**状态：已证明的条件几何定理。** 本篇把真正 Gauss–Codazzi 解的曲率
误差转成位置、法向、支撑、曲率与 reach 的完整预算。
参考位置和参考框架可以是实际数值重建后保存的有限函数；
不要求它们先成为一个精确等距浸入，也不需要其向量值二阶误差小。
所有误差上界仍须由实际连续数据证明，采样值不能充当它们。

## 1. 精确解与可计算参考

在一条带上令真实度量为
\[
 g=e(r)^2dr^2+a(r)^2d\theta^2,\qquad e,a>0.
\]
完整真实第二形式的正交分量为 \(A,B,C\)，并满足原 GC 方程和真实接口条件。
由实际尾部的框架向内重建
\[
 O=(X,Y,n),\quad O^TO=I,\quad \det O=-1,\qquad F_r=eX.
\]
法向取 \(n=Y\times X\)。径向方程是
\[
 O_r=O\Omega,\qquad
 \Omega=
 \begin{pmatrix}
 0&0&-eA\\
 0&0&-eB\\
 eA&eB&0
 \end{pmatrix}.
\tag{G.1}
\]
这与完整物理两迹拼接定理使用相同的方向和物理归一化。

令已指定、可计算的实参考函数为
\(\widehat F,\widehat O=(\widehat X,\widehat Y,\widehat n)\)，
并选择实参考系数 \(e_0>0,A_0,B_0\) 定义同形的反对称矩阵
\(\Omega_0\)。定义真实的连续残差
\[
 R_O=\widehat O_r-\widehat O\Omega_0,\qquad
 R_F=\widehat F_r-e_0\widehat X .
\tag{G.2}
\]
参考框架不必准确正交；参考位置的角导也不必准确等于 \(a\widehat Y\)。
这两件事均由最终真实 GC 解保证，不能反过来假设参考已经满足。

允许参考与真实径向度量略有不同，例如实际所选 \(\nu\) 与已保存中心参数
有一个已证小差。该误差在下文明确支付；它不把构造参数变化称为最终固定度量 flex。

## 2. 无指数放大的完整框架误差

令 \(E_O=O-\widehat O\)。直接相减 (G.1)–(G.2)：
\[
 (E_O)_r=E_O\Omega_0+O(\Omega-\Omega_0)-R_O .
\tag{G.3}
\]
由于 \(\Omega_0\) 反对称，其左右传播都是正交的；真实 \(O\) 的算子范数为1。
故对每个固定真实角 \(\theta\)，由外端 \(R\) 向内有
\[
 \|E_O(r,\theta)\|_{\rm op}
 \le \epsilon_O+
 \int_r^R\left(d_\Omega(s)+\rho_O(s)\right)\,ds
 =:\Theta(r),
\tag{G.4}
\]
其中假设已经完整证明
\[
\begin{aligned}
 \|E_O(R,\theta)\|_{\rm op}&\le\epsilon_O,\\
 \|R_O(s,\theta)\|_{\rm op}&\le\rho_O(s),\\
 d_\Omega(s)&\ge
 \sup_\theta\sqrt{(eA-e_0A_0)^2+(eB-e_0B_0)^2}.
\end{aligned}
\tag{G.5}
\]
最后一式准确等于这两个反对称矩阵之差的算子范数。
这一步没有 \(e^{\int\|\Omega\|}\) 的 Gronwall 费用，
也没有借参考框架精确正交来消掉误差。

若有限参考在径向接口有跳，则逐片积分 (G.3)，并将每个接口的
\(\|\widehat O(s+)-\widehat O(s-)\|\) 作为点源加入 (G.4)。
不能因为两端采样看起来接近而把准确 dyadic 跳当作零。

## 3. 位置误差与可保留相关性的双积分

记 \(E_F=F-\widehat F\)。用真实 \(X\) 的单位长度，准确写成
\[
 (E_F)_r=e_0(X-\widehat X)+(e-e_0)X-R_F .
\]
假设外端位置误差 \(\epsilon_F\)，
\(\sup_\theta\|R_F(r,\theta)\|\le\rho_F(r)\)，
则
\[
 \|E_F(r,\theta)\|
 \le\epsilon_F+
 \int_r^R\bigl[e_0(s)\Theta(s)+|e-e_0|(s)+\rho_F(s)\bigr]\,ds
 =:\Phi(r).
\tag{G.6}
\]
只需要径向的真实系数和残差，不需要给参考位置误差作两次角微分。

令 \(\ell_0(r,s)=\int_r^s e_0(t)\,dt\)。将 (G.4) 代回并交换非负积分：
\[
\begin{aligned}
 \Phi(r)\le{}&\epsilon_F+\ell_0(r,R)\epsilon_O\\
 &+\int_r^R \ell_0(r,s)\,[d_\Omega(s)+\rho_O(s)]\,ds\\
 &+\int_r^R[|e-e_0|(s)+\rho_F(s)]\,ds .
\end{aligned}
\tag{G.7}
\]
它可逐真实径向盒累计，保留外端曲率误差所乘的实际剩余长度。
径向位置跳也须以其完整范数加入相应点源；
框架跳还须乘它到观察点的 \(\ell_0\) 费用。

## 4. 互逆曲率变量直接给完整形算子

在 \(C\ne0\) 的同一物理 chart 中，令
\[
                       u=B/C,\qquad v=1/C.
\]
Gauss 式给准确恒等式
\[
 B=\frac uv,\qquad C=\frac1v,\qquad
 A=Kv+\frac{u^2}{v},
\]
\[
 S=\begin{pmatrix}A&B\\B&C\end{pmatrix}
   =\frac1v
       \begin{pmatrix}u^2+Kv^2&u\\u&1\end{pmatrix}.
\tag{G.8}
\]
它不使用 \(\sqrt{-K}\)，故可跨真实 \(K=0\)。
全部量仍是正交分量，不能把材料坐标二阶矩阵误当 \(S\)。

例如已证 \(|v_0|\ge\mu>0,\ |v-v_0|\le\varepsilon_v<\mu\)，
\(|u-u_0|\le\varepsilon_u\)，且此处 \(K\) 与参考相同，则
\[
\begin{aligned}
 |C-C_0|&\le\frac{\varepsilon_v}{\mu(\mu-\varepsilon_v)},\\
 |B-B_0|&\le\frac{\varepsilon_u}{\mu-\varepsilon_v}
       +\frac{|u_0|\varepsilon_v}{\mu(\mu-\varepsilon_v)},\\
 |A-A_0|&\le |K|\varepsilon_v
       +\frac{2|u_0|\varepsilon_u+\varepsilon_u^2}{\mu-\varepsilon_v}
       +\frac{|u_0|^2\varepsilon_v}{\mu(\mu-\varepsilon_v)}.
\end{aligned}
\tag{G.9}
\]
若 \(K\) 也有误差，可将
\(Kv-K_0v_0=K(v-v_0)+(K-K_0)v_0\) 的完整第二项加入，
或直接在同一有向区间盒上消费 (G.8)，避免丢相关性。

给定 \(k>0\)，真实绝对主曲率不超过 \(k\) 的准确条件是
\[
                         kI+S\succeq0,\qquad kI-S\succeq0.
\tag{G.10}
\]
可用同一闭盒的两个 \(2\times2\) 主子式证明。
无需从一个已知参考浸入的二阶向量差估计真实曲率。

## 5. 支撑、全局嵌入与真正 reach

若已完整证明
\[
 |\widehat F|\le R_0,\qquad
 \widehat F\cdot\widehat n\ge\sigma_0,
\]
则由真实 \(n\) 为单位向量，
\[
 |F|\le R_0+\Phi,\qquad
 F\cdot n\ge\sigma_0-\Phi-R_0\Theta.
\tag{G.11}
\]
公式来自
\((F-\widehat F)\cdot n+\widehat F\cdot(n-\widehat n)\)，
没有隐去一个参考法向归一化或额外乘积误差。

现假设全真实接口与反射已经构成一个连通闭 \(C^2\) 浸入，
并且在整张面上获得统一
\[
                  F\cdot n\ge\sigma>0,\qquad \|S\|_{\rm op}\le k.
\tag{G.12}
\]
径向投影 \(F/|F|\) 的微分可逆，因为径向向量不在切平面。
它是紧连通面到 \(S^2\) 的覆盖；\(S^2\) 单连通，故覆盖为一层。
因此 \(F\) 本身是星形嵌入，毋须先把参考图认作嵌入。

令 \(F_t=F+tn\)，且
\[
                         |t|<\rho:=\min(\sigma,1/k).
\]
其切向微分 \(I-tS\) 可逆，法向仍为 \(n\)，并且
\((F+tn)\cdot n>0\)。故每个 \(F_t\) 都是正的径向图
\(r_t(\omega)\omega\)。固定 \(\omega\) 对 \(t\) 微分并点乘 \(n\)：
\[
                    \partial_t r_t(\omega)
                     =\frac1{\omega\cdot n}>0.
\]
所以这些图对不同 \(t\) 互不相交，整个双符号法向管单射。
距原面小于 \(\rho\) 的点有最近点，最近连线为法向；
法向管单射使最近点唯一。因此
\[
 \boxed{\operatorname{reach}(F(M))\ge\min(\sigma,1/k).}
\tag{G.13}
\]
此证明只使用 \(C^2\) 正则性、紧性和已证的统一严格门。

若全域位置界为 \(R_*\)，则 \(D\le2R_*\)；
也可消费更好的实际直径上界。只要同一个最终面满足
\[
                    \min(\sigma,1/k)>.03D_{\rm upper},
\]
即得到所需 reach 比例。不同子段或不同参数对象的界不能混在一起。

## 6. 同一族的可见位移与固定握持

若两个最终相位端点与各自完整参考像的点值差统一不超过
\(\varepsilon_0,\varepsilon_1\)，并且某个参考端点见证满足
\[
 \operatorname{dist}(\widehat F_1(p),\widehat F_0(M))\ge d_*,
\]
则完整集合的 Hausdorff 距离有
\[
       d_H(F_1(M),F_0(M))\ge d_*-\varepsilon_0-\varepsilon_1.
\tag{G.14}
\]
参考像不必事先嵌入，但距离下界必须针对整张连续参考像；
只在腰环或有限点云上求最近点不够。

同理
\[
 \operatorname{diam}F_0(H)
 \ge\operatorname{diam}\widehat F_0(H)-2\varepsilon_H .
\]
闭 \(H\) 的内点与逐材料点全相位固定，仍由实际平端/标记拼接实现；
不能由直径估计自动得到。含反射非全等仍须在同一个最终族上使用完整
四个固定标记及其实际几何预算。

本篇提供可实际消费的几何接口，不宣称当前有限候选已经满足 (G.4)–(G.14)，
也不把局部 GC 存在、有限边值成功或采样几何当作闭面定理。
