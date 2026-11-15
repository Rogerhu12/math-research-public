# 设计：只消费完整 h 轴 sharp action 系数，不重编第四 forcing

日期：2026-11-15。**已实现独立 consumer，并仅通过 14 项小人工检查；真实目标尚未运行。** 对应 R148 的单一后继门，由根代理接入一次公开 Actions。不得将本设计或人工开发回执视作新的成员、非成员或正性结果。

## 1. 唯一目标和必要完整项

固定真实轴 $k=\omega=k_s=\cdots=0$，记 $u=h_s,a=h_{ss},j=h_{sss}$。在每个完整模式 $-4,-2$ 上，原 $v_4$ 在此轴的结构是

$$v_4=\beta(h)u j+A(h)a^2+C(h)u^2a+Q(h)u^4.$$

真实平端分部积分逐步给

$$\bar A=A-\beta,\qquad\bar C=C-\partial_h\beta,$$

$$\widehat Q_{4,\mathrm{axis}}(h)
=Q(h)-\frac13\partial_h\bar C(h)
-\mathcal B_{m_{2,\mathrm{axis}}(h)}(N_{2,\mathrm{axis}}(h)).
\tag{1}$$

这里 $m_2=u^2m_{2,\mathrm{axis}}$、$N_2=u^2N_{2,\mathrm{axis}}$，二者的速度平方已在定义中除去。$\mathcal B$ 是原 R83 完整两模式响应，外槽和内槽保持不交换；不是只取 pure Lie 公式。

唯一新目标为

$$\mathcal D_0=\Pi_{-2}[h^{-6}(\log h)^0]\widehat Q_{4,\mathrm{axis}},\qquad
\mathcal K_0=\mathcal D_0+\frac{25}{9}J.
\tag{2}$$

R148 只保证任一权 $-2$ 正仿射字符有 $\ell(\mathcal K_0)\ge0$。本设计不先给 $\mathcal D_0$ 或 $\mathcal K_0$ 的数值、原式 hash 或符号。

## 2. 轴上矩阵精简：只需两个未约化 N2 系数

直接把 $k=\omega=0$ 代入 R73 的准确点态八矩公式，可得

$$\boxed{
m_{2,\mathrm{axis}}(h)=\frac1{8h^4}E_{r_1}-\frac1{8h^2}E_{t_1}.
}\tag{3}$$

一个直接手算核对是：此时 $z=\xi,d=h\omega-k=0$，尾系数为 $r_0=1/(8h),r_2=h/8$，$\lambda=h_s\xi/h^2$。二次速度项 $-\lambda(r_i)_s$ 分别给 $+u^2\xi/(8h^4)$ 和 $-u^2\xi/(8h^2)$，且局部 $A_2$ 同时给对应的 $r_1+t_1\xi^2$，其余六矩坐标为零。

记未约化的完整外槽第三势系数

$$\mathcal N_{-2}=[h^{-2}(\log h)^0]N_{2,\mathrm{axis}},\qquad
\mathcal N_{-4}=[h^{-4}(\log h)^0]N_{2,\mathrm{axis}}.$$

由 $\mathcal B$ 对两个槽线性，所需最后一项准确只是

$$
[h^{-6}(\log h)^0]\mathcal B_{m_{2,\mathrm{axis}}}(N_{2,\mathrm{axis}})
=\frac18\mathcal B_{E_{r_1}}(\mathcal N_{-2})
-\frac18\mathcal B_{E_{t_1}}(\mathcal N_{-4}).
\tag{4}$$

因此只形成两个新的完整响应，不形成其余 N0/N2 系数的整套响应。特别，不以“势会在端部消失”或 pure 投影入像来删掉 (4)。$\mathcal N_{-2},\mathcal N_{-4}$ 均按原根保留，不预设它们属于 $\mathcal W$。

对原 $v_4$ 若已发记录确实没有相关 log 项，(1) 简化为

$$
\mathcal D_0=\Pi_{-2}\left[
 Q_{-6}+\frac53 C_{-5}+\frac{20}3\beta_{-4}
-\frac18\mathcal B_{r_1}(\mathcal N_{-2})
+\frac18\mathcal B_{t_1}(\mathcal N_{-4})\right].
\tag{5}$$

未来实现须先从真实记录核这个无 log 前提；若存在 log，使用 (1) 的完整 Laurent/log 微分，不能默删导数产生的常数项。固定 k、ω 后取 h 微分不会把已删除的正 k/ω 幂变回轴值。

## 3. 只读三个已完成输入，不重建旧数学

### A. 完整导数因子

原 run 43651096112，source 2259b57065cfad67682f4c4319885fd5334c4f76，lane local_fourth_derivative_factors。

目录：`notes/actions-43651096112-1-local_fourth_derivative_factors/`。

- 主报告 `local-fourth-derivative-factors.json`：5477 B；SHA256 42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927。
- receipt：33580 B；SHA256 6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e。
- 完整原根 gzip `local-fourth-derivative-factors-original-expressions.json.gz`：2132064 B；SHA256 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a。
- 原 JSON：11864540 B；SHA256 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。
- 原 producer：22205 B；SHA256 02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf。

十键顺序是 $(h,k,\omega,u,w,a,b,\log h,j,\ell)$ 的幂。只选择轴上对应 $uj,a^2,u^2a,u^4$ 的已发 v4 根，以及 N2 的轴上 $u^2h^{-2}$、$u^2h^{-4}$ 根。完整记录缺项只有在已核完整导出语义下才解释为原式零。

先从 `pointwise_matrix_original_coefficients` 验证 (3) 的有限有理元数据，再用 `old.decode_expressions` 只还原被选原根；不调用 `raw_potential`、`new_local_generators`、旧 forcing compiler 或 W 生成器。

### B. 已证 weight −2 完整响应块

原 run 43653293263，source 2f0add61f44365d713abf836beaa8b0be2806a3d，lane g_translation_successor，order 3。

- 主报告 `G-third-translation.json`：25014 B；SHA256 b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3。
- receipt：34619 B；SHA256 a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523。
- `G-third-translation-original-expressions.json.gz`：157782 B；SHA256 226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e。
- 原 JSON：889438 B；SHA256 eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7。

它已包含全部 50 个原响应两模式和 $N^3G$；原已证依赖给 40 个真实响应基。直接消费这 40 个根与 $N^3G$，不重新构造任何已完成响应、不重跑 10 条旧依赖。

### C. 已证新 J

原 run 43654534244，source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b，lane acceleration_layer_mixed。

- 主报告 57753 B；SHA256 baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745。
- receipt 35241 B；SHA256 3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494。
- `acceleration-layer-mixed-original-expressions.json.gz`：318634 B；SHA256 b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e。
- 原 JSON：1909429 B；SHA256 7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38。

只读 candidate 0 的两个原根，hash 分别为：

~~~text
-4  2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3
-2  70f565c5c6d7075ec99bc383fc0ee66e914aff06fbc273bc3c1e431123d7c979
~~~

R136 已证明 J 加到上面的 41 维块后真实独立，所以所考察的准确 42 维空间为

$$\mathcal E_{-2}=\mathcal R_{8,-2}+\mathbb RN^3G+\mathbb RJ.$$

## 4. 未来一次目标消费的输出语义

若根代理决定部署，只形成 (1)–(5) 和 $\mathcal K_0$ 两个完整模式。可复用既有 `blocks.full_response(ring, ThirdOperator(...), quadratic_basis)`，但只调用 (4) 的两项。原槽顺序、正 profile 次数右原函数和两模式的相同有理系数保持。

首先准确保存新目标及两项新响应的原根、来源 key、原 hash、总度与真权。随后只尝试 $\mathcal D_0\in\mathcal E_{-2}$；阳性必须从原两模式表达式重新构造线性关系并 fresh 核零。$\mathcal K_0$ 由其定义同时导出，不另运行一次成员目标。一个未消正规形余项仅标为未决，不自动启动更大扫描，也不授予函数非成员。

若有准确关系

$$\mathcal D_0=R+cN^3G+dJ,\qquad R\in\mathcal R_{8,-2},$$

则 R148 对权负二正字符给 $(d+25/9)\ell(J)\ge0$。若 $d+25/9<0$，结合 $\ell(J)\ge0$，可严格迫这一类字符在 J 上为零；若 $d+25/9\ge0$，此一维门与已知条件相容。即使前者成立，也不自动证明一般正泛函杀 J 或 J 已有实际有符号控制。

这里只计划一条与真实正性门直接对应的原式关系；不遍历剩余九个 A/H 候选，不重启已完成 G 链或 pure 幂尾扫描。

## 5. 预算和保存边界

本次实际预算为 180 秒、1024 MiB RSS 软轮询；已有 R136 完整解码与新目标实际峰值为 255.16 MiB，本次要同时保留三个原式输入和新的两次收缩，因此不把预算降到贴近已有峰值的范围。若被真实复杂度触发，应保已完成输入绑定和原根输出，不能把预算退出当作关系不存在。主报告目标小于 90 KB，完整推导/关系另存 gzip；新原根上限 2.5 MB、完整报告上限 2.0 MB、加主报告合计预留 4.59 MB。

该研究预算尚未实际执行，不能写成已测研究性能。新增人工检查只使用小 Laurent/log 状态项和非对称三槽 toy；真实目标运算仍只在本公开仓库 Actions。

## 6. 已冻结源码、人工状态与最小 CLI

新源码 `scripts/literature_h_axis_sharp_coefficient.py`：31222 B，SHA256 7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b。没有修改任何旧生产者或消费器。

人工回执 `notes/h-axis-sharp-development.json`：6525 B，SHA256 2cd976e7c348463bbf3bdc53ef2d0fa9b1363a0b20b3e931ed1071d7215ebbe3。14 项均通过，0.010226289 秒，15.125 MiB；只包括新轴 IBP、log 常数项、两矩收缩方向、非对称外槽/内槽及原式保存接口，未读真实输入，未编译或评价研究目标。

完整人工报告 gzip 为 `h-axis-sharp-development-complete-report.json.gz`：2024 B，SHA256 aa5fcf1f5113cd21b94951e11a7ce0c24df6b92a05615ea38d173301c408e680。公开实际 job 可以复用这些人工源身份，或同 job 执行下列人工命令；不存在额外的新数学门。

~~~bash
python topics/visible-flex-new-mechanism/scripts/literature_h_axis_sharp_coefficient.py --toy-only --output /tmp/h-axis-sharp-output/h-axis-sharp-development.json
python topics/visible-flex-new-mechanism/scripts/literature_h_axis_sharp_coefficient.py --output /tmp/h-axis-sharp-output/h-axis-sharp.json
~~~

所有实际输入路径、run、source 和 SHA 默认已经硬绑定到第 3 节，不需要在命令行复制一长串可变参数。路径可显式覆盖以适配检出，但身份不能变化；only-repository Actions 门在进入真实消费前检查。

实际输出固定为主报告 `h-axis-sharp.json`、完整报告 `h-axis-sharp-complete-report.json.gz` 与新原式 `h-axis-sharp-original-expressions.json.gz`。原式先保存，报告大小问题不能静默删除已完成的原根或把未决升级为负结论。

当前仍没有这条 D0 目标的实际研究输出、成员关系或非成员证书。

