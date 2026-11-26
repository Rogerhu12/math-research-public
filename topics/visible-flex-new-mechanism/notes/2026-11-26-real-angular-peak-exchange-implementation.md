# 2026-11-26：保留完整均匀约束并加入实际角峰的续接范围

本文件是新实现及新请求的静态说明，不是数值收据。本地只写源码、解析 AST、核对小配置与原日志身份；首次求值、接口检查、FFT、参数微分、定位、优化和全部扫描都在同一次公开 Actions 科学 job 内计费。该范围不改 R566 物理模型，也不重跑已登记的早期恢复。

## 1. 为什么需要这个新算子

联合预算 run `45777140827` 已自然结束，两 lane 原始收据分别在 `2026-11-26-joint-budget-b030-first-metric-receipt.md` 和 `2026-11-26-joint-budget-b038-metric-and-peak-cap-receipt.md`。B030 的全细网 eta 为 `0.9398189402917945`，B038 为 `0.8536143165549589`，二者有限细网几何原始违规为零，但末次都因尚未采用的 `3072` 角约束提议超过原上限而结束。旧结果没有连续几何、完整 reach 或固定 g 收敛证明。

这次分开三个对象：完整周期 primitive 与均值 E 的 FFT 规则、原已采用的 `1536` 角实际约束、另外观测到的真实角峰坐标。单纯将均匀角数继续翻倍会把求积分辨率和约束峰位置混为同一件事。本次保留每个旧均匀约束，在其外增加明确的 `(s, theta)` 轨道点；完整 `3072` 角细网仍逐候选扫描。

## 2. 精确输入与范围

新请求 `computations/request-inverse-theta-peak-20261126.json` 内两份小配置都从上述原 stdout 的末态提取，绑定 source commit `384921b12780519b5af6ce02b44b83f8f1b5b924`、原 request、原日志、engine FINAL 和外层 FINAL 的 SHA256。它们是新计算输入，不把原始日志或大数组入 Git。

| lane | 原 job | 原 actual radial | 原 pending radial | 本次起始 radial | 原 trust 原样保留 | 已累计科学秒 |
|---|---:|---:|---:|---:|---:|---:|
| B030 | 139763424593 | 119 | 119 | 119 | 0.10546875 | 366.50969979800004 |
| B038 | 139763424928 | 121 | 122 | 122 | 0.015625 | 1335.867809179 |

每份 `q` 恰为原 81 个浮点参数；所有原 actual 和 pending 径向位置并入新起始网格。原 actual 角数为 `1536`，原 pending `3072` 明确只作为仍需完整细扫的提议，绝不称为旧 run 已优化的约束。物理参数、完整全局参数盒、R=1.012、Y=1−0.6R、tau=0.06R 均保持。两 lane 仍分别为 `(p,q,r)=(.85,.15,.15)` 和 `(.8,.18,.2)`。

mean-E floor `.25`、det floor `.10`、工作余量 `.001` 和有限扫描原始可行阈值 `1e-8` 均与来源相同。前两者是所选径向参数规范中的限制，不是 README 规定的数值。每轮改变 q 仍会改变设计度量，不能计为固定 g 的精化。

## 3. 任意角值与参数微分

新 `inverse_r566_angular_oracle_20261126.py` 绑定已发布 block source；`UniformJetModel` 保持原空间一二阶 jet 公式，只额外留出 primitive、径向 profile 和完整均匀 Ebar。九个实 primitive 分量的 FFT 系数用于任意角 Fourier 求和。T、Ts、Tss、Ttheta 继续用原解析物理式计算。

因此该算子评价的是明确的数值 primitive 与解析切向量混合近似；不能从有限 FFT 得到未经证明的 `Ptheta=T`。可打印的 `Ptheta−T` 等观测差也不是连续 Fourier 尾界。均值 E 与其全部参数导数始终来自完整均匀网格，绝不从非均匀峰点取平均。位置、E/F、法向和曲率的参数列沿相同公式用 forward AD 分块计算。

旧均匀点只有在浮点角坐标与原 uniform theta **严格相等** 时才直接 gather 原已准备值；不把附近非均匀点吸附到网格。非均匀点才做 O(M) Fourier 求和。核心准确弧长反演按唯一 theta 复用；同一轨道内的实际点、行身份与求和成本仍保留。

`CombinedRows` 的实际约束是原完整均匀轨道最小行与全部已采用新角峰的四点轨道行。均匀 orbit-min 等价保留原所有浮点不等式；先选择实际最小行，再加 Phase I 的共同 slack，保持原浮点分支次序。新峰不进入隐藏 selected pool，也不替换旧均匀行。参数列按 16 个方向拼接；每块重建值必须与 value-only 的实际行相符。

## 4. 定位、接受与交换

每个外层的细网包含全部 actual radial、相邻中点和原 97 点基础径向网格，角数为 `3072`。完整场先扫描，随后对观测到的角峰括区做 bounded scalar 定位。几何场用工作违规；metric 使用两支光滑谱量 `(sqrt(e²+4f²+1e-24)±e)/2`。每次评价四个真实反射轨道点，原采样值较大时保留原点。

该有限括区定位不证明不存在漏峰。candidate 上限、定位未自然完成、固定 FFT 的观测差超阈值都会作为未完成 checkpoint 记录；不能因为定位器 success 就升级为连续认证。全细网的有限原始几何门继续有效，实际观测到的连续角点还可收紧该门及 eta。只有完整细扫和这些观测点均可行、定位完成且 eta 实际下降，才接受 metric 改善。

回调同时记录当下 actual 约束与 fine 扫描，防止未可行的中间 SQP trial 反复被同一种已覆盖违规打断。对新峰的立即交换阈值是：

- Phase I 几何：`covered=max(sigma, actual 同组工作违规, 0)`；
- Phase II 几何：`covered=actual 同组工作违规`；
- Phase II metric：`covered=max(t, actual 同支 metric 峰, 0)`。

几何峰超过 `covered+max(1e-6,.05*covered)`，或 metric 峰超过 `covered+max(1e-7,.02*covered)`，才立即把新的实际点交给下一约束集。超过 sigma/t 或零工作余量、但尚未越过上述间隙的小峰保留 pending，在后端自然返回后批量加入。处于原 actual 违规覆盖内的新点不会仅因绝对值为负而触发重启。初始观测的未覆盖小峰同样先记入 pending，给后端真正执行步的机会。

发生网格交换本身不自动缩 trust。实际接受的步达到当前局部盒九成时才扩为 1.5 倍；自然后端无改善、无新峰时才减半。原 trust 输入不重置。每轮实际盒、下一提议、自然 OptimizeResult、最后未接受 trial 和保留 q 分开打印。pending 只有下轮实际建模后才成为 actual；最后未采用的坐标仍在最终提议中。

在相同 q、相同径向位置的 `1536/3072` 嵌套均匀值上，记录 e/f 差、相对 Ebar 差与 tau 乘曲率差，任一超过 `1e-7` 就明确要求另立 FFT 分辨率范围。这个比较只是已观测求积差，不能称为 Fourier 尾界，也不抵消实际几何违规。

## 5. 一次正式 run 内的必要接口核对

首次实际优化前，在同一个已启动科学 job 内做一次原均匀算子 parity：7 个径向位置乘 13 个角位置，逐项比较 E、F、e、f、det、Ebar 和两主曲率，最大差阈值 `1e-9`。随后在偏移 `.371` 个角步的真正非均匀点做一次全参数方向导数检查：差分步 `1e-6`，相对 L2 差阈值 `3e-4`。检查成本在本次科学总时长及底层计数中；成功后自动继续这同一次优化，不另开预检 run，不要求额外确认。

静态交叉审已核过 CombinedRows 的参数列、extra 列、release 后 value 身份，以及 actual/pending/backend/trial 的分离。审读发现的 Phase I 与 metric 中间 trial 覆盖遗漏已修正。定位汇总计数明确命名为 completed localizations；中途截止的底层点求值仍由 oracle totals 和总 wall elapsed 支付，不冒称未发生。

## 6. 发布与未完成边界

新 workflow 为 `.github/workflows/visible-inverse-theta-peak-20261126.yml`，两 lane、最大并发 2、job 50 分钟，沿用已发布 stdlib runner。每 job 科学开始前真实 pull 公共/私有两仓并核规则；Python 3.12.14、numpy 2.3.5、scipy 1.17.0 和两个 Actions SHA 固定。只写原始 stdout，不产 artifact、cache、Git 写入。

科学总段为 2400 秒，保留最后 30 秒做实际末 q 的重新扫描与可完成的角峰观察。所有入口重建、接口检查、完整细扫、FFT、AD 块和定位计时均计入新成本。时间到只产生明确未完成 checkpoint，继续工作须用其实际末 q、actual 和 pending 身份接续，不能当课题完成。

这次公开源码及请求没有证明 eta 达 `1e-6`、固定 g 精化、全时闭体嵌入或全 pair reach；也不把局部曲率和镜像必要行称为完整 reach。真正的连续认证和闭体全部门仍欠，主线继续。
