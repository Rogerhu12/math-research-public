# R149 补充：全正侧实际有符号受迫解的公共计算与独立端口列

在完整 low193 逆及其四个实际源图成立时，GBC、SAR、NPG 与 FHC 接受的是同一 $\delta_*$、真实 $r_*,R=25/8$、原 $S_m$、同一套独立均值和原 $577\times2$ 两列物理源。给定任意全局系统的端口 $u_j$，把其正侧解写成 Newton 或 $\nu$ 的已知 affine 常数，加上各独立端口的线性响应。数值入口保留原 97+96 物理约束、$c=9/10$ 的真实截面以及整段 $[0,r_+]$ 的普通径向角向 $L^2$。

原 signed 两列与边界/shell Gram 由 SAR、GBC 在完整原有向模型上计算；两个已知高态逐一返回完整 low 行。真邻域取 $\rho=10^{-7}$ 和原 endpoint 限制，NPG 闭合两种原物理边界判据；根已付的 NPG 四个精确差分费按其真实整件读取。若实际 body 或物理终端门失败，则完整小结论保留第一个不满足的物理门和此前各原物理输出，截止于这一分支。若 NPG 真门通过，对 $p=0$ 的两列已知源，由 FHC 的实际 SCAP.3 入域和完整高度单位列求 $F_{\rm sel}$。在两列 $u=0$ 处的结果仅指各自的 affine 常数。

对于每个进一步独立单位端口 $u_j$，把同一正侧线性方程中两列已知源置零。使用 QN.43 七列及 QN 的原 raw/body/outgoing 表，再通过 NPG 的实际低 body、两个外端及其图的提升得到 $(B_j,b_j,a_j)$。低点源与两段 negative source 各按 NPG 的原单位支付，$S_c=U_a+s$。同一体截面给
$$
 K_j\le4400B_j+.332C_{H,j}+3.6S_{b,j}+.005\|f_{L,j}\|+J_j.
$$
令暂时独立的单位高度输入产生 $H_{\rm pos}$，令 $Y_j$ 为独立高度零时某一物理输出的上界。FHC 真实反馈门的裕量 $\mu=1-t>0$ 时，下面是同一全函数分支：
$$
 F_j={e_{f,j}+\omega G_{d,j}+.11\omega K_j\over\mu},
 \qquad Y_j^{\rm sel}\le Y_j+Y(H_{\rm pos})F_j .
$$
额外高度或显式曲率输入分别令 $e_{f,j}=1$ 或 $G_{d,j}=1$；其余各单位方向这两项为零。于是若 $n_0$ 为真 $\nu$ 已知列的全负窗费用，完整匹配所需的物理 readout 满足
$$
\|q_\nu-Z\|_{L^2([0,r_+];L^2_\phi)}
 \le n_0+\sum_j n_j^{\rm sel}\|u_j\|.
$$
$n_j^{\rm sel}$ 由其自身的无已知源方程算出，对这些线性纯输入不重复加入 $s_\delta$ 或 $Z(c)$。全部 root、Robin、mean、height、严格及近根 ordinary 源和原跳分别存为物理列。实际全局 $u_j$ 由 waist、holonomy、截面及世界位置方程决定。

公共入口在已有真实 GG、WSS、NPG-fees、WHN 与 FHC 整件完整时才能生成。原 WSS 固定镜像、Haswell 与必要 native 重构和 320-bit 有向源在同一 job 私盘恢复；原 7,728 片、61 整块、完整源字节和 index 都要同原 SHA 一致。另用 GG 的原主机算术环境、原 320/384 位模型、完整 21 原件、已有 81 段的原载体，再用 GRR 核完整图/node/matrix journal。只有通过全部原始字节资格后，才运行新的矩阵积分及两列/独立端口观测。一次公共 job 共用时间、全部私盘和内存上限。原 GG 46135063788/1 的第一项科学目标在第 82 个左格失败；该结果不产生本入口所需的全逆。其后经新证明得到的其他模型需要自身完整的入场合同。

[首发元数据器](../scripts/make_selected_physical_response_manifest.py) · [公共 worker](../scripts/fourfold_codazzi_selected_physical_response_public_worker.py) · [完整受迫 owner](../scripts/fourfold_codazzi_selected_physical_response_owner.py) · [独立物理列](../scripts/fourfold_codazzi_selected_independent_port_rows.py)
