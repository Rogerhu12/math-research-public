# R748　由一个材料高度重建每个试步的整张周期实物

取 [R744](R744-scalar-height-development-true-cap-correction-and-thick-core-mode-exclusion.md) 的同一规定度量 \(g=E(r)\,dr^2+r^2d\varphi^2\)。本构造对未解标量方程的高度也给一张真正周期的物理面，能直接计算全部三 Gram 和真实二阶。真实无穷细胞的积分或其剩余界仍由每个实际输入支付。

## 从真实外帽向内的单次积分

高度 \(u(r,\varphi)\) 是完整材料圆上的实周期函数。令
\[
 s^2=1-u_r^2/E-u_\varphi^2/r^2>0,\quad
 A=\sqrt{E-u_r^2},\quad c=-u_ru_\varphi/A,\quad d=r\sqrt E\,s/A .
\]
于是 \(q=g-du^2=(A\,dr+c\,d\varphi)^2+d^2d\varphi^2\)。要求 \(u\) 在真实水平外帽有同一高度、径一导、径二导迹（选择外帽高度零）；\(E(b)=1,E'(b)=0\)。令
\[
 \beta(b,\varphi)=\varphi,\quad U(b,\varphi)=b e^{i\varphi},\quad
 B=\beta_r=\frac{c_r-A_\varphi}{d}
   =-\frac{E u_\varphi(u_{rr}-E'u_r/(2E))}{A^2r\sqrt E\,s},
 \qquad U_r=Ae^{i\beta}. \tag{1}
\]
\(B\) 周期，故 \(e^{i\beta}\) 和 \(U\) 全为字面周期。取 \(F_o=(\Re U,\Im U,u)\)；任何合域的 \(u\) 都给 \(|(F_o)_r|^2=E\)，无需预设其余两 Gram。径向积分式本身只需相应连续的二阶数据；下文微分角方向时另外要求 \(u,u_r,u_{rr}\) 各自的所需角导连续、有界，具体 \(u\) 至三角导，\(u_r,u_{rr}\) 至二角导。有限 Fourier 系数为 \(C^2\) 的输入满足此条件。一般仅 \(C^2(r,\varphi)\) 不自动提供所有这些混导。曲率恒等式先对足够光滑的分片输入证明，再对有相同二阶迹、联络相接且相应弱导可积的结取极限。

写 \(G=(d_r+cB)/A,\ W=\beta_\varphi-G,\ H=U_\varphi-(c+id)e^{i\beta}\)。R744 的联络在此余标架下为 \(-B\,dr-G\,d\varphi\)，故 \(W_r=B_\varphi-G_r=K_q A d\)。直接交叉微分 (1) 得 \(H_r=i A e^{i\beta}W\)。若 \(\mathcal D\) 为 R744 (1) 的左减右，即
\[
 \mathcal D=\bigl(u_{rr}-E'u_r/(2E)\bigr)\bigl(u_{\varphi\varphi}+r u_r/E\bigr)
 -\bigl(u_{r\varphi}-u_\varphi/r\bigr)^2
 -K_g(r^2E-r^2u_r^2-Eu_\varphi^2),
\]
则
\[
 W_r=-\frac{\mathcal D}{r\sqrt E\,s^3},\qquad
 H_r=iA e^{i\beta}W,\qquad W(b)=H(b)=0. \tag{2}
\]
这些等式中表面三阶高度的径向导数已抵消；也可先从联络微分得到，再用 R744 的内禀曲率恒等式代换。真实混合与周向 Gram 缺陷准确为
\[
 \Delta g_{r\varphi}=\Re(\overline{U_r}H),\qquad
 \Delta g_{\varphi\varphi}=2\Re(\overline{(c+id)e^{i\beta}}H)+|H|^2.
\]
因此一项标量残差通过两次真实径积分控制整张材料，而外帽已固定时 \( \mathcal D=0\) 自动给全圈无旋转/平移单值展开。

更具体，设 \(D_*(r,\varphi)\) 上界 \(|\mathcal D|\)，\(a_*\ge A,\ e_*\le E,\ \sigma_*\le s\) 为同一场的正界。则
\[
 \frac{|H|}{r}\le
 \delta(r,\varphi)=\frac1r\int_r^b\!\left(\int_r^t a_*(\xi,\varphi)d\xi\right)
 \frac{D_*(t,\varphi)}{t\sqrt{e_*(t)}\,\sigma_*^3(t,\varphi)}\,dt .
\]
相对 Gram 的算子范数至多 \((1+\sqrt2)\delta+\delta^2\)，因为相对混合至多 \(\delta\)，周向线性差至多 \(2\delta\)，二次差至多 \(\delta^2\)。R738 的 \(a_*\le1.69,\ e_*\ge1,\ r\ge.075\) 给全段粗估 \(\delta\le3.16\,\sup|\mathcal D|/(\inf s)^3\)。普通格网最大值不得充作此处的连续上界。

## 内真实帽、两支与所有物理两阶

内帽真实姿态是 \(C+rR_y(\vartheta)e_r(\varphi)\)，其中 \(C=(C_x,0,C_z)\)。给 \(u,u_r,u_{rr}\) 在 \(r=a\) 分别为 \(C_z-a\sin\vartheta\cos\varphi,\ -\sin\vartheta\cos\varphi,\ 0\)，角向导数随真迹；\(E(a)=1,E'(a)=0\)。对反射对称 \(u\)，\(U(r,-\varphi)=\overline{U(r,\varphi)}\)。\(u_\varphi(r,0)=0\) 迫 \(\beta(r,0)=0\) 且该母线 \(U_r>0\)。若 (2) 残差处处为零，则内圈平面发展只差一个定向平面刚运动；反射迫转角为0或 \(\pi\)，正实径导选0，平移沿 \(x\)。确切
\[
 L_\pm=\int_a^b\sqrt{E-u_r(r,0\text{ 或 }\pi)^2}\,dr,\quad
 L_++L_-=2(b-a\cos\vartheta),\qquad C_x=(L_--L_+)/2.
\]
每个 \(L_\pm\) 都是该材料母线真实的水平投影长度，不能换成目标 \(\int\sqrt E\)。若 \(C_x\) 另有指定必须单独相等。这些必要条件对未解场也可实际逐项读。

一般试步只保证外帽。为了在有残差时就能使用真闭壳门，定义
\[
 P_a=C_x+a(\cos\vartheta\cos\varphi+i\sin\varphi),\quad
 T_a=\frac{\cos\vartheta\cos\varphi+i\sin\varphi}
           {|\cos\vartheta\cos\varphi+i\sin\varphi|},\quad
 R=T_a e^{-i\beta(a,\varphi)},\quad U_i=P_a+R[U-U(a,\varphi)] .
\]
\(R\) 是角函数，计算一二角导不使用带割线的反正切。因为两端出发的 \(\beta_r\) 是同一 \(B\)，此式**正是**从真实内帽出发的径向发展；不需第二次 ODE。固定 \(C^2\) 截止 \(\chi\) 在真内领为1、真外领为0，在中央有限段连接，置 \(V=U+\chi(U_i-U)\)，\(F=(\Re V,\Im V,u)\)。内外实际六项皆与真刚件相接。特别在平帽边 \(A_r=B=0\)，\(V_{rr}=0\)；一阶平迹和其角导给实物 \(V_{r\varphi},V_{\varphi\varphi}\)。此结论需要输入的两个高度端口都准确；仅给较小的端口误差时，仍须实测并保误差。

令 \(D=U_i-U\)，则 \(V_r=U_r+\chi D_r+\chi'D\)，
\(V_{rr}=U_{rr}+\chi D_{rr}+2\chi'D_r+\chi''D\)，
\(V_{r\varphi}=U_{r\varphi}+\chi D_{r\varphi}+\chi'D_\varphi\)，
\(V_{\varphi\varphi}=U_{\varphi\varphi}+\chi D_{\varphi\varphi}\)。
其中 \(U_{rr}=e^{i\beta}(A_r+iAB)\)，
\(U_{r\varphi}=e^{i\beta}(A_\varphi+iA\beta_\varphi)\)；
对 (1) 再作两次真实材料角导，积分 \(U_\varphi,U_{\varphi\varphi}\)。拼合带须从 \(V\) 重新读全部三 Gram、全部曲率及两法向，(2) 的单侧误差界不能直接给拼合后的界。一个可用的全带一基界是
\[
 e_r=(|\chi D_r|+|\chi'D|)/\sqrt E,\quad e_\varphi=|\chi D_\varphi|/r,\quad e=e_r+e_\varphi .
\]
若单侧相对 Gram 缺陷上界为 \(\eta\)，则新缺陷至多 \(\eta+2\sqrt{1+\eta}\,e+e^2\)。连续版要求这里所有范数亦有全点包围。真解且两姿一致时 \(R=1,D=0\)，两支为同一图，截止带不增加方程。

## 真计算接口的资格

给定拥有上述径二阶、角高导的同一个高度场和固定 \(E,E'\)，对每一径分段以 Gauss 原函数累积 \((B,B_\varphi,B_{\varphi\varphi})\) 和 \((U_r,\partial_\varphi U_r,\partial_{\varphi\varphi}U_r)\)。内端复相位一次即恢复另一支。每个真实材料点均可输出单侧、实内侧、拼合实际六阶数据（位置、两个一导、三个二导）、两个独立 Gram 缺陷、完整标量残差、全径累积的 \(W,H\) 和直接由真 \(U_\varphi\) 读取的 \(H\) 交叉差。末级需保正 \(s\) 域、实际内外六迹、两真实圆心位姿、双框正图、曲率、偏移、实际跨件支撑及 \(D\)。一段有限 Gauss 评价和由它计算的 \(\int|\mathcal D|\) 都是普通近似。若源给每胞残差/正图连续界，应另走 (2) 的非负上积分，绝不把只采节点当全点证书。

R738 的已付旋量真场处在辅助角参数，材料 \(\varphi\) 须用其本身的正速度反求；包括实际 \(u,u_r,u_{rr}\) 以及所需角导，不能把 \(\psi\) 直接当 \(\varphi\)。若改作有限材料 Fourier 高度，应在同一真实场付一次保二阶的迁移并比较全部高度端迹与六项；不同材料角网的投影各自误差另列。两侧 \(n\ge0\) 真尾若被截在有限切口，则须带该整段的径向积分、所有三类角原函数的余界或确切端传播。仅一项深尾高度上界不足以重建端姿和两阶。当前这项坐标定理没有授予 R738 已成功、R745 已得双核或任何新有限角力学结论。

