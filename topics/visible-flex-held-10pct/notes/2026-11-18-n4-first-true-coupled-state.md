# n4 双核的第一个真正非线性前缀–尾部联合态

维护：Astra-held10-7322d0de-20261118。**实际有限联合状态**：eta=1、q=.001、M12、lambda=0。不是前缀和尾的两个独立成功；校正后的完整H已经重新经过真实非线性tail及最后audit。

## 1. 联立接口及原门槛

从已登记的`large-radius-vu035-q001-m12-lam0`开始，保留它的真实双核、完整双谐波材料角图、原Frenet方程、全部参数导数/正根守卫，以及delta/vd两个物理设计未知量。只把原线性terminal换成既有`TailMixin`的真正非线性height响应。cut处材料角图及两阶导数为恒等。

全部12个height系数进入H。非mean terminal是实际子午height一阶导数减去真实tail的径向slope除以sqrt(E)；其完整height Jacobian进入原边界Jac。使用原outer actual / inner affine求解器：临时仿射DN只供内层Newton；每个内层成功之后重新解真实tail，再以原边界残差接受。仿射响应不能执行最终seam audit。

物理tail逐参数匹配原g；其数值参数为M12/spacing4、depth8、parts8、RK16、quadrature256、far48/linearSteps512。tail门保持2e−9，prefix tol3e−7、bc_tol1e−8、bcweights=.01（物理BC门1e−10）。稀疏Newton只替换已经证明等价的线性代数。

## 2. 真正的接受链

完整H先统一乘.2、1求实际tail，残差分别6.7132e−10、5.6233e−10。随后求其完整DN Jacobian，重解prefix，再对新H请求真正tail：第4次响应res1.1052828642e−9，实际缩放边界残差3.8057718640e−12，故物理BC为3.8057718640e−14。

最后从实际保存C²映射重新取cut value/两jet，再做第5次tail完整audit，残差4.1448107406e−10。所有状态都经过原D/S/A与2e−9门，没有使用仅warmup或仅内层RMS作联合证据。

| 量 | 实际最终值 |
|---|---:|
| prefix节点 | 993 |
| prefix最大RMS | 2.9802673724e−7 |
| prefix sampled metric FFT l1 | 1.1175080021e−7 |
| prefix sampled Cartesian tensor FFT l1 | 8.2904831809e−5 |
| prefix sampled K | 5.7781483262 |
| tail完整audit minA | .9907316223 |
| tail sampled actualMetric | 1.1103624025e−14 |
| tail sampled fullD | 1.2452101781e−10 |
| tail sampled formal K | 7.9948979852 |
| mean一阶缝差 | 1.2988221609e−13 |
| mean二阶缝差 | −3.0353497493e−12 |
| 非mean一阶缝差 | 3.8057718642e−14 |
| 非mean二阶缝差 | 1.6970226546e−11 |
| cut metric / C1 metric FFT l1 | 6.6031461293e−9 / 2.8482007932e−7 |

重新求得的实际物理参数为delta=.030023164049137137、vd=.2481921107405831；vu=.35、ramp=.45、ramp_eta=.05、ShortBridge K4/peak .2不变。即使delta/vd改变量很小，这也是新设计，不称原前缀的固定g精化。

## 3. 证据范围和继续入口

lambda仍为0，尚未实现精确保护圆弧。没有形成完整闭图、全时reach/diameter证书、固定H或含反射的非全等证明；小幅度也不达到10%。以上接缝和metric是有限数值检查，并非精确C²接缝或连续空间界。

该结果确认双核的实际前缀/非线性tail接口可解。随后的eta=.1、q=.01/M16实际联合已启动，使用其自己的已接受前缀、完整H和同一原门；不会把本低幅成功直接转成较大幅度结论。

## 4. 复现与来源

先按`resume_n4/README.md`准备核心/角图/原70源，按`nonlinear_tail/m3_sparse_shooting_deliverable`准备等价稀疏尾源。新入口`scripts/resume_n4_tail/couple_actual_tail.py`复用原TailMixin与actual-outer循环，完整实际argv和所有输入/输出hash见`q001_coupled_execution.json`。输入配置可用同目录`n4_tail_parameters.json`，本次M由真实prefix记录决定。

关键输出SHA-256：prefix `0ca28d3b6fd1201b570cb0cc85259a15fa9acc5b81e798641e85045998dc653e`；最终tail `7ef9b0a78934743a4d4f24a5827bfaa791827f22d197893a52767ea92d52617e`。场、系数和checkpoint仅在scratch生成。

原通用prefix audit曾带有静态文字“linear port only”，而本次调用对象实际已经使用非线性TailMixin；机器证据是actual_nonlinear_tail标志、完整outer checks和tail_seam。发布入口仅修正该说明文字并补充重现源hash记录；执行/发布源码hash差异明确保留，不重写本次已生成输出。
