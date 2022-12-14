window.onload = function () {

    $(".preloader").addClass("preloader-remove");
    $(".body_cl").addClass("body_scroll");

    //якоря и скролл
    const anchors = document.querySelectorAll('a[href*="#"]');
    if (anchors.length > 0) {
        for (let anchor of anchors) {
            if (document.querySelector('.main_bg') && anchor.getAttribute('href').length === 6) {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault()
                    const blockID = anchor.getAttribute('href').substring(2)
                    try {
                        document.getElementById(blockID).scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        })
                    } catch (TypeError) {

                    }
                })
            }
            if (document.querySelector('._atr_anchr_scrl') && anchor.getAttribute('href').length === 23) {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault()
                    const blockID = anchor.getAttribute('href').substring(17)
                    try {
                        document.getElementById(blockID).scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        })
                    } catch (TypeError) {

                    }
                })
            }
            // todo: доделать скрол на разных станицах через определние атрибута href в зависимости от страницы
            // if (document.querySelector('._atr_anchr_scrl') && anchor.getAttribute('href').length === 20) {
            //     anchor.addEventListener('click', function (e) {
            //         e.preventDefault()
            //         const blockID = anchor.getAttribute('href').substring(11)
            //         try {
            //             document.getElementById(blockID).scrollIntoView({
            //                 behavior: 'smooth',
            //                 block: 'center'
            //             })
            //         } catch (TypeError) {
            //
            //         }
            //     })
            // }

        }
    }
    full_page_lice();

    function full_page_lice() {
        let l_item = document.querySelectorAll(".lice_img");
        let l_img = document.querySelectorAll(".full_page_licences");

        for (let i = 0; i < l_item.length; i++) {
            l_item[i].id = `lic_${i}`;
            l_img[i].id = `lic_img_${i}`;
        }
        // l_item.forEach(function (value, key, ) {
        //     this.id = `lic_${key}`;
        // })
        //
        // l_img.forEach(function (value, key, ) {
        //     this.id = `lic_img${key}`;
        // })
    }

    // window.addEventListener("scroll", function () {
    //     let scroll = this.scrollY;
    //     // console.log(scroll);
    //
    // });


    document.addEventListener("click", documentAction);

    //delig
    function documentAction(e) {
        const targetElement = e.target;

        //открывашка меню в хедере
        if (targetElement.classList.contains('Menuarrow')) {
            targetElement.closest("._head_items").classList.toggle('_hover');
            console.log(targetElement.closest("._head_items").querySelector(".Menuarrow").classList.toggle("_hover"));
        }
        if (!targetElement.closest("._head_items") && document.querySelectorAll("._head_items._hover").length > 0) {
            document.querySelectorAll("._head_items._hover").forEach(function (el) {
                el.classList.remove("_hover");
                el.querySelector(".Menuarrow").classList.remove("_hover");
            });
        }

        //открывашка лицензий
        if (targetElement.classList.contains('lice_img')) {
            let id = targetElement.id.substring(4);
            document.getElementById(`lic_img_${id}`).classList.toggle("open");
            document.querySelector('.body_cl').classList.toggle('remScrl');
        }
        if (targetElement.classList.contains('full_page_licences')) {
            targetElement.classList.remove('open');
            document.querySelector('.body_cl').classList.remove('remScrl');
        }

        //открывашка формы в вакансиях
        if (targetElement.classList.contains('bt_form')) {
            document.querySelector('.full_page_rezum').classList.toggle('open');
            document.querySelector('.body_cl').classList.toggle('remScrl');
        }
        if (targetElement.classList.contains('full_page_rezum')) {
            targetElement.classList.remove('open');
            document.querySelector('.body_cl').classList.remove('remScrl');
        }

        // открывашка формы на главной
        if (targetElement.classList.contains('btn_form')){
            document.querySelector('.form_container_main').classList.toggle('open');
            document.querySelector('.img_form').classList.toggle('open');
            setTimeout(function () {
                document.querySelector('.boom_img').classList.toggle('open');
            }, 100);
            document.querySelector('.boom_img').classList.toggle('open');

        }

    }

    //
    // const form_container = $(".form_container_main");
    // const bnts_open_form = [$(".btnarr_open_form"), $(".botton_container"),]
    // const img_formm = $(".img_form");
    // const move_form_wigth = form_container.width() - bnts_open_form[0].width();
    // const boom_img = $(".boom_img");
    // let form_sost = true;
    // bnts_open_form[1].on('click', function (e) {
    //     e.preventDefault();
    //     boom_img.css({
    //         opacity: "1",
    //         visibility: "visible",
    //     });
    //     setTimeout(function () {
    //         boom_img.css({
    //             opacity: "0",
    //             visibility: "hidden",
    //         });
    //     }, 100);
    //     open_close_form();
    // });
    // bnts_open_form[0].on('click', open_close_form);
    // function open_close_form() {
    //     if (form_sost === false) {
    //         form_container.css({transform: "translateX(0px)",});
    //         img_formm.css({transform: "rotateZ(0deg)",});
    //         form_sost = true;
    //     } else {
    //         form_container.css({transform: `translateX(${move_form_wigth}px)`});
    //         img_formm.css({transform: "rotateZ(180deg)",});
    //         form_sost = false;
    //     }
    // }


    let position = 0;
    const slidesToShow = 1;
    const slidesToScroll = 1;
    const container_ = $('.slider_container');
    const track_ = $('.slider_track');
    const item_ = $('.slider_item');
    const btn_nxt = $('.bt_nxt');
    const btn_prev = $('.bt_prev');
    const item_count = item_.length;
    const counter_slider_class = $(".count_sl_now");
    const itemWidth = container_.width() / slidesToShow;
    const slider_counter_block = $(".hid_sl_cnt");

    const move_position = slidesToScroll * itemWidth;

    let count_sl_now = 1;

    slider_counter_block.css({
        opacity: "0",
    });

    $(".count_sl_all").text(item_count);
    counter_slider_class.text(count_sl_now);

    container_.mouseenter(function () {
        slider_counter_block.css({
            opacity: "1",
        })
    });
    container_.mouseleave(function () {
        slider_counter_block.css({
            opacity: "0",
        })
    })

    function btnCheck(position) {
        if (position >= 0) {
            $('.bt_prev_ar').css({
                display: 'none',
            })
            $('.fal_bt_prev').css({
                opacity: '50%',
                display: 'block'
            })
        } else {
            $('.bt_prev_ar').css({
                display: 'block',
            })
            $('.fal_bt_prev').css({
                opacity: '0%',
                display: 'none',
            })
        }

        if (position <= -(item_count - slidesToShow) * itemWidth) {
            $('.bt_nxt_ar').css({
                display: 'none',
            })
            $('.fal_bt_nxt').css({
                opacity: '50%',
                display: 'block'
            })
        } else {
            $('.bt_nxt_ar').css({
                display: 'block',
            })
            $('.fal_bt_nxt').css({
                opacity: '0%',
                display: 'none',
            })
        }
    }

    item_.each(function (index, item_) {
        $(item_).css({
            minWidth: itemWidth,
        });
    });

    btnCheck(position);


    function Set_pos(position) {
        track_.css(
            {transform: `translateX(${position}px)`}
        )
        btnCheck(position);
    }

    btn_nxt.click(function () {
        position -= move_position;
        counter_slider_class.text(++count_sl_now);
        Set_pos(position);
    });


    btn_prev.click(function () {
        position += move_position;
        counter_slider_class.text(--count_sl_now);
        Set_pos(position);
    });


    ssssssl();

    function ssssssl() {


        const timeoutMainSlider = 10000;
        let position_slidermain = 0;
        let sliderMainIndex = 0;
        let newIndex = 0;
        const slidesBox = $(".slider_container-mainbg");
        const slide = $(".wp_roller_it-mainbg");
        let size;
        const sliderMainMax = slide.length;

        try {
            autoSlider();
        } catch (TypeError) {

        }


        function autoSlider() {
            slidesBox.css({
                transform: `translateX(${position_slidermain}px)`
            });

            slidesBox[0].addEventListener("transitionend", function () {
                try {
                    if (slide[newIndex - 1].id === "firstClone") {
                        sliderMainIndex = 0;
                        size = $(".wrapper-mainbg").width();
                        position_slidermain = -sliderMainIndex * size;
                        slidesBox.css({
                            transition: "none",
                            transform: `translateX(${position_slidermain}px)`
                        });
                        newIndex = 0;
                    }
                } catch (TypeError) {

                }
            });

            // todo: отключать слайдер при скроле вниз
            // todo: обнулять слайдер если меняется ширина экрана
            if (sliderMainIndex >= sliderMainMax - 1) {
                newIndex++;
            } else {
                sliderMainIndex++;
                size = $(".wrapper-mainbg").width();
                position_slidermain = -sliderMainIndex * size;
                newIndex++;
                slidesBox.css({
                    transition: 'all 1.2s ease-in-out'
                });

            }
            setTimeout(autoSlider, timeoutMainSlider);
        }

    }


    let sliderMainPostIndex = 0;
    let positionSliderMainPost = 0;
    const slidesToShowMain = 3;
    const sliderTrackMainPost = $(".slider_track_main");
    const slideritemMainPost = $(".slider_item_mainPost").css({
        minWidth: `${100 / slidesToShowMain}%`
    });
    const btn_prevMainPost = $(".arrow-left");
    const btn_nxtMainPost = $(".arrow_right");

    const MaxSlides = slideritemMainPost.length;

    function check_btnsMainPost() {
        if (sliderMainPostIndex >= MaxSlides - slidesToShowMain) {
            btn_nxtMainPost.css({
                opacity: "50%",
                cursor: "unset",
            });
            btn_nxtMainPost.removeClass("ar_hov");
        } else {

            btn_nxtMainPost.css({
                opacity: "1",
                cursor: "pointer",
            });
            btn_nxtMainPost.addClass("ar_hov")
        }
        if (sliderMainPostIndex <= 0) {
            btn_prevMainPost.css({
                opacity: "50%",
                cursor: "unset",
            });
            btn_prevMainPost.removeClass("ar_hov")
        } else {

            btn_prevMainPost.css({
                opacity: "1",
                cursor: "pointer",
            });
            btn_prevMainPost.addClass("ar_hov")
        }
    }


    btn_nxtMainPost.on("click", function () {
        const itWidth = slideritemMainPost.width();
        if (sliderMainPostIndex < MaxSlides - slidesToShowMain) {
            btn_nxtMainPost.css({
                opacity: "1",
            });
            sliderMainPostIndex++;
            positionSliderMainPost = -itWidth * sliderMainPostIndex;
            sliderTrackMainPost.css({
                transform: `translateX(${positionSliderMainPost}px)`
            });
            check_btnsMainPost();
        }
    })
    btn_prevMainPost.on("click", function () {
        const itWidth = slideritemMainPost.width();
        if (sliderMainPostIndex >= 1) {
            sliderMainPostIndex--;

            positionSliderMainPost = -1 * itWidth * sliderMainPostIndex;
            sliderTrackMainPost.css({
                transform: `translateX(${positionSliderMainPost}px)`
            });
            check_btnsMainPost();
        }
    });
    check_btnsMainPost();


    second_part();

    function second_part() {
        const sel_swtch = document.querySelectorAll(".second_part_sw_txt_item");
        const sel_tx_switch = document.querySelectorAll(".sec_sw_txt_item_ls_3");
        const sw_img = document.querySelectorAll(".sec_sw_img_block");
        for (let i = 0; i < sel_tx_switch.length; i++) {
            sel_swtch[i].id = `swt_${i}`;
        }

        sel_swtch.forEach(function (el) {
            el.addEventListener("click", function () {
                let act_remove = document.querySelectorAll(".second_part_sw_txt_item.activ_cl_sw_txt")[0];
                let act_remove_txt = document.querySelectorAll(".sec_sw_txt_item_ls_3.active_sw_txt")[0];
                let acr_remove_img = document.querySelectorAll(".sec_sw_img_block.active_sw_img")[0];
                act_remove_txt.classList.remove("active_sw_txt");
                act_remove.classList.remove("activ_cl_sw_txt");
                acr_remove_img.classList.remove("active_sw_img");
                this.classList.add("activ_cl_sw_txt");
                let index = Number(this.id.substring(4));
                sel_tx_switch[index].classList.add("active_sw_txt");
                sw_img[index].classList.add("active_sw_img");
            });
        });
    }

    f4_part();

    function f4_part() {
        const sel_swtch = document.querySelectorAll(".f4_switch_txt_item");
        const sel_tx_switch = document.querySelectorAll(".f4_sw_txt_item_ls_3");
        for (let i = 0; i < sel_tx_switch.length; i++) {
            sel_swtch[i].id = `swf_${i}`;
        }

        sel_swtch.forEach(function (el) {
            el.addEventListener("click", function () {
                let act_remove = document.querySelectorAll(".f4_switch_txt_item.activ_cl_sw_txt")[0];
                let act_remove_txt = document.querySelectorAll(".f4_sw_txt_item_ls_3.active_sw_txt")[0];
                act_remove_txt.classList.remove("active_sw_txt");
                act_remove.classList.remove("activ_cl_sw_txt");
                this.classList.add("activ_cl_sw_txt");
                let index = Number(this.id.substring(4));
                sel_tx_switch[index].classList.add("active_sw_txt");
            });
        });
    }


    //


    let containers_th_part;
    initDrawers();

    function initDrawers() {
        // Get the containing elements
        containers_th_part = document.querySelectorAll(".item_third_container");
        setHeights();
        wireUpTriggers();
        window.addEventListener("resize", setHeights);
    }

    window.addEventListener("load", initDrawers);

    function setHeights() {
        containers_th_part.forEach(container => {
            // Get content
            let content = container.querySelector(".tab_third_part");
            // Needed if this is being fired after a resize
            content.removeAttribute("aria-hidden");
            // Height of content to show/hide
            let heightOfContent = content.getBoundingClientRect().height;
            // Set a CSS custom property with the height of content
            container.style.setProperty("--containerHeight", `${heightOfContent}px`);
            // Once height is read and set
            setTimeout(e => {
                container.classList.add("height-is-set");
                content.setAttribute("aria-hidden", "true");
            }, 0);
        });
    }

    function wireUpTriggers() {
        containers_th_part.forEach(container => {
            // Get each trigger element
            let btn = container.querySelector(".lice_name_thirdPart");
            // Get content
            let content = container.querySelector(".tab_third_part");
            btn.addEventListener("click", () => {
                container.setAttribute(
                    "data-drawer-showing",
                    container.getAttribute("data-drawer-showing") === "true" ? "false" : "true"
                );
                content.setAttribute(
                    "aria-hidden",
                    content.getAttribute("aria-hidden") === "true" ? "false" : "true"
                );
            });
        });
    }


    paralaX_for_pict();


    function paralaX_for_pict() {
        if (window.innerWidth > 1336) {
            let sw_img_move = document.querySelectorAll('.sw_img');
            let sw_img_move_1 = document.querySelectorAll('.sw_img_1');
            for (let i = 0; i < sw_img_move.length; i++) {
                window.addEventListener('mousemove', ev => {
                    let x = ev.clientX / window.innerWidth;
                    let y = ev.clientY / window.innerHeight;
                    if (sw_img_move) {
                        sw_img_move[i].style.transform = 'translate(-' + x * 40 + 'px, -' + y * 40 + 'px)';
                    }
                });
            }
            for (let i = 0; i < sw_img_move_1.length; i++) {
                window.addEventListener('mousemove', ev => {
                    let x = ev.clientX / window.innerWidth;
                    let y = ev.clientY / window.innerHeight;
                    if (sw_img_move_1) {
                        sw_img_move_1[i].style.transform = 'translate(+' + x * 40 + 'px, +' + y * 40 + 'px)';
                    }
                });
            }
        }
    }

    //

}

//
// $(function () {
//     $("._button_").click(function () {
//         alert("bt")
//     })
// });

// $(function () {
//   console.log(Math.round(window.scrollY));
//   let posTop = Math.round(window.scrollY);
//   let h = window.innerHeight;
//   alert(h);
//   alert(posTop);
//   if (posTop>h) alert("111");
// })
