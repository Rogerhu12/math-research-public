# 自由切口 Schur v2 的 root 全文复核

审查者：/root，2026-11-09。状态：**完整条件式推导 PASS**。此为方法审查，无新增 root、flow、DN 或 prefix 求解调用；不认定新非线性解存在或收敛。

## 1. 冻结对象与完整范围

审阅 tail-free-cut-schur-method-v2.md 全部八节，SHA256 `479252a0fbaa8ba4d7299acee038a4b49f22a40e8f3c6cc4b4cff50eb6f16802`，以及 sources-v2.json 的全部源文件绑定。root 先全文读旧稿，再逐字比较 v2；唯一改动是纠正“零内部残差推出全部 b=0”的单向性措辞。19 个公式和其余证明未变。旧稿保留，不能把审查结论反标到未经修正措辞。

复核原 trial-core 的 stage 输出/portRatio、evaluate、correction、末端坐标转换、cutJets、tangentGraphAtCut、heightJetJacobian；原 moment root 的归一化；原 TailMixin 的 terminal、bc_jac、seam_audit。其余固定接口条件、尺寸、prefix 消元的全部代数在正文逐项读完。

## 2. 尾 forcing 和双向等价

原残差是 R_n=Phi_n(y_{n+1})−y_n，因此 Newton 行给 delta y_n=J_n delta y_{n+1}+R_n，而不是减 R_n。深端 e=Pi_d−G_deep Q_d 给 b_d=−e。分块代入后，t=B b_next+R_Q，u=D b_next+R_Pi；X=A+B Gamma_next 可逆时，Gamma=(C+D Gamma_next)X^{-1}、b=u−Gamma t。原 correction 中 gs/bs/Gi/t 完全采用该符号。

逐层回代 delta Q_next=X^{-1}(delta Q−t)、delta Pi_next=Gamma_next delta Q_next+b_next，满足全部原内部行与深端行；反向由同一代入唯一得到。没有省略不为零的 shooting forcing。零 R,e 足以推出全部 b=0；反向不成立，例如 b_next=0 时取非零 R_Q 并令 R_Pi=Gamma R_Q，即可相消。v2已准确排除此误推。

## 3. 实际物理规范化

完整 stage 的 momentum 行已除原 portRatio，故其 J 不应再次缩放。node0 的 cut 局部 root 需要 diag(I,rho I) 转成 cell0 engine 动量；cutJets 正是如此。普通余弦物理高度为 c^4 Q，斜率为 m_j^2 c^3 Q_j+sqrt(2) w_c L_j。root target 的 kappa 含 orientation sqrt(12) mu0/(sqrt(2)c^4 w_c^2)，与原 engine 一致。

隐微分必须用包含均值的整个 M+1 维 moment 矩阵。rho 因子只出现在对节点 Pi 的链式导数中。直接从 f_Q=(r_x/c)[(m^2−4)Q+sqrt(2)w L/c^3] 推出 S=4c^3Q+(c^4/r_x)f_Q，交叉核无符号或频率差异。沿图有限差分 heightJetJacobian 只有收缩后导数，既不能替代两个偏导块，也不含内部 b。

原 TailMixin 请求 H=sigma q_g Z_b，terminal 为 (q_g f_z−S_t/sqrt(E))/bcweights。因此 S_p=sqrt(E)q_g f_z，不再乘 sigma；斜率匹配与原 terminal 只是可逆正行缩放。gauge 固定，实际 support 参数经 inlet 和 prefix 方程进入 z；定理没有漏掉该自由参数。

## 4. prefix forcing、维数及最终系统

移去 M 个尾斜率行，F_p 有 k−M 行；加入 M 个物理高度行恰为方阵 J_p。若其可逆，a_p=−J_p^{-1}(F_p,r_h)，B_p=J_p^{-1}(0,c^4 I)，所以 delta z=a_p+B_p delta Q0。a_p 包含配点和边界的全部当前缺陷，不能因从旧 CP 开始而置零。

斜率行代入后 C_out=S_p,z B_p−S_Q，D_out=−S_Pi，r_out=r_s+S_p,z a_p。再代入尾 delta Pi0=Gamma0 delta Q0+b0，恰得 (C_out+D_out Gamma0)delta Q0=−r_out−D_out b0。双向回代覆盖 prefix、物理高度/斜率、全部 stage 与 Robin，无额外固定 H 条件。所有消元 chart 可逆时，完整系统非奇异与末矩阵非奇异等价。chart 失败不能推完整 Jacobian 奇异。

## 5. 可用范围与实施缺口

当前基点必须能评价每个原 root/flow；一个被 guard 拒绝的 trial 没有自动可用的 J。非零尾 forcing 使 Gamma0 只是该点的线性关系，不能称已解 DN 导数。自由 cut 会改变某个辅助固定 H 实验的边界布局，必须标作联合 warm；它保持的是完整 prefix/tail 匹配问题。

矩阵代数等价不证明 literal rounded 实现为真导数，不给条件数、非线性收敛或连续几何证书。源码未公开 forcing 消元数据，prefix collocation 的完整 J_p 装配与一次分解多右端、同源 cut 偏导均尚待实施。现 bc_jac 会再次调用 DN，不能用它而宣称绕过 DN。本文和本审查没有更改原 guard、容差、物理度量或验收门。
