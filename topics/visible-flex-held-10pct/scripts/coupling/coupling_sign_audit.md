# m=2 ShortBridge 与真实有限尾 DN：符号和接口审读

会话：`true_a_analysis`；2026-11-17。

复用来源是提交 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2` 的 `topics/visible-flexible-closed-surface/scripts/db6f-prefix-coupled.py`，SHA-256为 `37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a`。其 TailMixin、AffineTailForInnerBVP、solve_with_actual_tail 和 seam_audit 未改方程。新 `couple_smallcut.py` 只选择已有二重 prefix loader、ShortBridge 和指定的真实物理 tail worker。

## 1. 反射与一阶 BC

在 cut 上写 sigma=sign(dr/ds)，本主线 sigma=−1。尾 worker 以 r 为坐标，g=E(r)dr²+r²du²；其返回的高度、径向导数为 H、P。将 worker 曲面作整体竖直反射并平移：

\[
z_{phys}(s,u)=z_0+\sigma z_{worker}(r(s),u),
\quad r_s=\sigma/\sqrt E.
\]

若前缀非均值高度为 Z=q y_z，则 worker 的正确输入为 **H=sigma Z=−Z，全部 Fourier 分量同乘−1**。随后

\[
z_s=P(H)/\sqrt E,
\qquad R=q f_z(y,p)-P(\sigma q y_z)/\sqrt E.
\]

因此原 TailMixin 的不翻转 slope 输出是正确的。不能以假设非线性 P 为奇函数，替代一次实际的负向量求解。在线性极限 P(H)=D H，这恰好恢复原前缀的 q y′_z=sigma D q y_z/√E。

## 2. Jacobian 和二阶数据

对终端状态 y 求导，height 列上的修正为

\[
D_yR=q D_yf_z-\sigma q\,D_HP/\sqrt E.
\]

所以 sigma=−1 时，在高度列上是加 q D_HP/√E。原代码中的 `T[:,iz:] -= sigma*q*TJ/sqrt(E)` 与此一致；不应再加一次反射符号。

尾引擎 `heightJetJacobian` 以物理高度H为列，行顺序为 slope[M]、second[M]、meanSlopeCorrection、meanSecondCorrection、height[M]。它已经把内部 r⁴ 归一化除回去；适配器只取前 M 行，不再乘或除 r⁴。

又有

\[
r_{ss}=-E_r/(2E^2),\qquad
z_{ss}=\sigma\{Q/E+P r_{ss}\}.
\]

均值 slope、second 使用同样公式。cut 角 chart 必须为恒等映射至二阶；当前 m2 loader 和 ShortBridge 保留原实现这一条件。完整 Cartesian 二jet、尾的无限闭合和全族 reach 仍由独立几何审计支付。

## 3. 模式与初始化

当前实际频率为2,4,...,2M，tail `spacing=2`。首模线性端向量是

\[
\left[-w(rD_1-4)/3,\,1\right].
\]

新 hybrid D1约−185 时其 F/H约1.587。m=3 的公式含9和8，不可把三重 DN 的列重贴成二重标签。

新 q=.02 线性端口前缀虽有 H1约−1.44e−5，H2却约+7.94e−5；仅凭H1缩小17倍不能推断实际尾负担也缩小17倍。所有真实请求都用完整向量。

继承的 adaptive restart 在改变q时主要按整体幅度比例生成几何初猜，未保证每个高模按q的阶次重解。`--relax-linear` 可先用原有限线性DN在目标q重解前缀，再调用实际尾。这一步明确标作初始猜测准备，不会被接受为非线性耦合成功。

## 4. 接受标准与复现边界

默认沿用原程序的外层真DN/内层仿射DN：每次内层前缀求解后，都对新完整H作真实非线性DN求解，并重新检查原始BC；只有达到原bc_tol才接受。仿射对象禁止 seam audit。`--actual-every-query` 可选择原直接调用模式。

warmup可选整向量线性缩放，或原各模幂缩放；两者均仅是求解初值路径，最终请求必须等于完整目标向量。每次真实worker请求、返回、失败、配置与来源哈希均保存在仓库外。

物理输入核验包括：全部声明的物理参数、modes/spacing、cut五项jet，以及worker ready的线性DN与输入port一致。移出source目录的worker显式设置VISIBLE_FLEX_SOURCE_TOPIC；client的源哈希仍从原client目录读取，实际worker另记SHA。冻结的stage1 factory SHA为 `a8fa355e984c2eff4de7e2ff7f654b04da1cbfa53f9591e7137f0c79b56b12ab`。

目前只是有限 Fourier、有限深度的耦合入口；任何solver success都不自动成为课题完成证书。
