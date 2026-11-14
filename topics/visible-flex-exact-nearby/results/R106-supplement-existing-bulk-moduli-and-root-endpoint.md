# R106 补充：旧全角模数的准确复用范围及真实根端有限项

2026-11-12，constructive-route。

本篇区分两个实际状态：R99 与完整真射线的根端费用已经由准确 BigInt
执行通过；旧 R50 bulk 的逐叶模数提取器已经保存，但原大叶文件暂时不能在
失联的本地执行器读取，故本篇没有伪造新的全 bulk 数值。旧角平均本身
始终不被解释为非均值密度界。

## 1. 已完成的真实根端预算

同一个准确 $\delta_5\pm10^{-9}$ 族，R99 的实际完整 frame 小摘要为
notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier-summary.json，
SHA256 8c13c40e1ea65eb05a97eaeb79cba1ab49f8ebe734ad598d0b382a0afe6890bf。
它逐字段来自完整真实报告
notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier.json.gz，
SHA256 d6f74fae93df5db08f5ac26b2ba196112ce73812643ad125278c42a8ca345439。
R99 证明和原复格报告给所有相关场在物理角带 $S=1/256$ 上的实际复模界；
这里没有把有限 Fourier 多项式改称真实根场。

沿用 R106 grounded 补充的
$$
u=\log U,\qquad t_0=e^{-u/4},\qquad
e_{\rm root}=\frac{\sigma}{8}u_\theta
=-\frac{\sigma}{2}\frac{(t_0)_\theta}{t_0}. \tag{106E.1}
$$
这是根部有限常数，不是可丢掉的平均零项。所有角导数均为物理 $\theta$
导数。R99 的 $A_1$ 权为 $(1+4|n|)$，因此
$$
\|e_{\rm root}\|_{A_0}
\le\frac12\|t_0\|_{A_1}\|1/t_0\|_{A_0}<1.146. \tag{106E.2}
$$
执行器为保守起见又将小摘要各档 norm 后列的 error 加回一次；
即使重复支付这笔已经包含的误差，(106E.2) 仍通过。
完整准确有理上界的可读值为 1.1453936234127853。

完整真射线证书 R106T 给当前标签带 $s=1/1024$ 上
$$
|\Im\Theta|<s_\theta=
\frac{8221101}{8000000000},\qquad
|J|=|\Theta_x|<J_*=\frac{8223669}{7812500}. \tag{106E.3}
$$
两者覆盖整个参数盒和全部实时间，包括真实两个根。
R99 给
$$
|t_0|\le M_t=1.4821328185498714447021484375,\qquad
|1/t_0|\le M_i=0.830902836285531520843505859375
$$
于完整物理带 $S$。因 $s_\theta<S$，对 $t_0$ 作准确 Cauchy 界得到
$$
|e_{\rm root}\circ\Theta|
\le\frac{M_tM_i}{2(S-s_\theta)}<214,\qquad
|(e_{\rm root}\circ\Theta)J|<226. \tag{106E.4}
$$
后一个有向有理值为
$2919058076316839561810037/12964117619394098495488$。
它是完整当前标签带上的界，而 (106E.2) 只在物理根标签的 Wiener
范数中成立；没有免费把两个范数或 frame 等同。

同理 R99 的真 $Y_0'$ 复模给 R106 完整首相位根减项
$$
c_0=\frac5{16}Y_0',\qquad
|(c_0\circ\Theta)J|
\le\frac5{16}\|Y_0'\|_S J_*<0.098. \tag{106E.5}
$$
该不等式的准确上界为
$525183806578761/5368709120000000$。
这是完整 $\mathcal F/\mu$ 的 $c_0$。若使用约化 grounded 密度
$D_g$，其对应首项是 $-Y_0'/16$，不可混用二者的符号和五倍系数。
$h_1,s_1$ 所需的第二个根减项以及连续根有限部仍未在此支付。

源码 scripts/fourfold_subprincipal_root_endpoint_exact.mjs 逐字验证
R99 小摘要、R99 证明和 R106T 已执行报告的 SHA，严格核对整个参数
身份，再执行五个准确有理门。实际新报告为
notes/2026-11-12-R106-root-endpoint-budget.json。
本次已在 V8 执行相同纯实现；Node 文件包装尚未在 native 运行。

## 2. 旧 R50 bulk 曾支付的量究竟是什么

已全文读核 frozen BulkTarget.angular_domain 和 exact-affine bulk
运行源。它们在每个实际径向闭叶先执行
$$
M_I=\sup_{r\in I,\ |\Im\theta|\le\sigma/4}|D(r,\theta)|,
$$
然后将 $M_I$ 用于角 Fourier alias 费用，最后才对原函数求角平均。
对应的真实字段名是 complex_angle_density_bound，不是 integral。
这里 R50 的 $D$ 正是 R106 的 reduced_density；其完整角散度和端点
仍另由 R106 公式保留。

两份完整旧 collector 小文件可由接口读取，但它们的 selected_cells
只复制了有符号角平均积分，没有复制 $M_I$。真正 $M_I$ 保存在原叶文件：

| 旧点输入 | 原始文件大小 | 原 SHA256 |
|---|---:|---|
| notes/2026-11-12-beta-exact-affine-step3-bulk-part00.json | 170678 B | c073d072bfb25c7774a8749b8d37b7ec6539e64a1203c59d96d8d1613a249b09 |
| notes/2026-11-12-beta-exact-affine-step3-bulk-part01.json | 150668 B | 1df2298ed56599e6e068118787ffb24937a9d92ff8ea36366f2c1b49d36e0d79 |

其完整 collector 为
notes/2026-11-12-beta-exact-affine-step3-complete-enclosure.json，
SHA256 179c58121f284ea16c2522e4e3f1493f109f857d37be5de60cf445bbe8750680。
它记录 167 个原始 common span、257 个准确选择叶、
固定 cut $268136140016943/1125899906842624$ 与腰 cap $2^{-20}$。

旧点是
$$
p_3=-7832869216826619/4611686018427387904,
$$
并非当前 $p_0=\delta_5$。另一个 uniform bulk 只覆盖
$p_3\pm10^{-8}$，也不包含当前盒。不能只因都叫 D5 就把旧复角模界迁移。

## 3. 可从现有证书准确支付的实角迁移

完整真导数覆盖是在 $\Delta_5=p_3\pm10^{-5}$、固定物理 $r$ 上支付
$\int\sup_{\theta\in\mathbb R}|\partial_pD|\,dr$，不是仅支付
$\partial_p\langle D\rangle$。其独立准确汇总为
notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json，
SHA256 1047f423a77d07aa14093b17fcf28376243857d8bf738b5d62f65f0f3dea7923。
这里需要的是字段 bulk_upper，不是加入 collar 后的 beta_derivative。

该覆盖明确是**实角**覆盖。它可以准确推出
$$
\int_0^{r_c}\sup_{\theta\in\mathbb R}|D(r,\theta,p)|\,dr
\le I_3+\epsilon B_{\rm bulk},\qquad
\epsilon=|p_0-p_3|+10^{-9}, \tag{106E.6}
$$
其中 $I_3$ 为旧点真实全角模数累计，包含腰 cap；
$B_{\rm bulk}$ 来自上述整盒真实 $D_p$。本次已有小输入的准确 BigInt
运算验证 $\epsilon<10^{-5}$ 且
$$
\epsilon B_{\rm bulk}<21/1000. \tag{106E.7}
$$
这笔实角参数费不大，但 (106E.6) 不给当前参数上的复角带。
旧真 $D_p$ 报告的连续角域仅为实圆，所以没有把 (106E.7) 解释为
复角迁移或 Sobolev 高频尾证书。

若 $I_3$ 已从原大叶提取，那么由准确径向反射与 R106T 的全时 $J_*$，
在 $[-r_c,r_c]$ 上真实主积分满足
$$
\left|\frac12\int_{-r_c}^{r_c}(D\circ\Theta)J\,dr\right|
\le J_*(I_3+\epsilon B_{\rm bulk}) \quad(x\in\mathbb R). \tag{106E.8}
$$
这里正负半面的模界因子 2 与 R106 的 $1/2$ 准确抵消；$J_*$ 仍保留。
这仅是主积分，不包括角散度积分、根有限部或端点。

## 4. 已保存的只读准确提取器

scripts/fourfold_subprincipal_extract_saved_bulk_moduli.py 使用标准库
Fraction，读取上述两个大原叶和已经发布的小 collector。它逐 SHA 检查原
文件、几何源及 origin/direction，按 collector 实际选择的 source_part
恢复每个原始 span 的全部闭叶，再检查准确无缝覆盖；不凭文件名取最新叶。
每个显示球的上端点都再加上其显示半径，随后只对 $M_I|I|$ 作准确求和。

它另外读取完整真导数 transfer 原报告并核对准确中心、整盒、cut、origin、
direction 和独立 audit 的 original_report_sha256。腰部旧费用只授实角；
旧复模仍只授 $p_3$ 上 $[2^{-20},r_c]$。
输出会同时明确 new_center_complex_strip_proved=false、
angular_divergence_and_endpoint_paid=false、root_finite_parts_paid=false。

因执行器仍不可用，**本次没有运行这个提取器，也没有输出 $I_3$ 的数字**。
文件与全部准确入口已保存，恢复执行器后只需读原字节，完全无需重算几何：

~~~sh
python scripts/fourfold_subprincipal_extract_saved_bulk_moduli.py \
  --topic . --out /tmp/R106-saved-bulk-moduli.json
~~~

如果输出超过 100000 B，使用 .json.gz 路径；源严格拒绝无压缩大文本。
原大叶只能通过获准的本地/CI 文件系统读取，不能借小文件接口分片绕过。
